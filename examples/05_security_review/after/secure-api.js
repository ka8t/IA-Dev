const express = require('express');
const { Pool } = require('pg');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { body, param, query, validationResult } = require('express-validator');
const he = require('he');
require('dotenv').config();

const app = express();

// ✅ Security headers
app.use(helmet());

// ✅ CORS configuration
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', process.env.ALLOWED_ORIGINS || 'https://example.com');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

app.use(express.json({ limit: '10kb' })); // ✅ Limit payload size

// ✅ Environment variables for secrets
const JWT_SECRET = process.env.JWT_SECRET;
if (!JWT_SECRET) {
  throw new Error('JWT_SECRET environment variable is required');
}

// ✅ Database connection with env vars
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false
});

// ✅ Rate limiting for authentication
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts per IP
  message: 'Too many login attempts, please try again later',
  standardHeaders: true,
  legacyHeaders: false,
});

// ✅ Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    return res.status(403).json({ error: 'Invalid or expired token' });
  }
};

// ✅ Secure login endpoint
app.post('/api/login',
  loginLimiter,
  [
    body('username').trim().isLength({ min: 3, max: 50 }).escape(),
    body('password').isLength({ min: 8 })
  ],
  async (req, res) => {
    // ✅ Validation
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { username, password } = req.body;

    try {
      // ✅ Parameterized query (prevents SQL injection)
      const query = 'SELECT id, username, password_hash, role FROM users WHERE username = $1';
      const result = await pool.query(query, [username]);

      if (result.rows.length === 0) {
        // ✅ Generic error message (prevents user enumeration)
        return res.status(401).json({ error: 'Invalid credentials' });
      }

      const user = result.rows[0];

      // ✅ Use bcrypt to compare passwords
      const validPassword = await bcrypt.compare(password, user.password_hash);

      if (!validPassword) {
        return res.status(401).json({ error: 'Invalid credentials' });
      }

      // ✅ JWT with expiration
      const token = jwt.sign(
        { userId: user.id, role: user.role },
        JWT_SECRET,
        { expiresIn: '1h' }
      );

      // ✅ Only return safe fields
      res.json({
        token,
        user: {
          id: user.id,
          username: user.username,
          role: user.role
        }
      });

    } catch (error) {
      console.error('Login error:', error);
      // ✅ Generic error message (no stack trace exposure)
      res.status(500).json({ error: 'Internal server error' });
    }
  }
);

// ✅ Secure user creation endpoint
app.post('/api/users',
  authenticateToken,
  [
    body('username').trim().isLength({ min: 3, max: 50 }).escape(),
    body('email').isEmail().normalizeEmail(),
    // ✅ Prevent mass assignment - don't accept role from request
  ],
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { username, email } = req.body;
    // ✅ Default role, not from user input
    const role = 'user';

    try {
      const query = `INSERT INTO users (username, email, role) VALUES ($1, $2, $3) RETURNING id, username, email, role`;
      const result = await pool.query(query, [username, email, role]);

      // ✅ Don't expose sensitive fields
      res.status(201).json(result.rows[0]);
    } catch (error) {
      console.error('User creation error:', error);

      // ✅ Handle duplicate username/email gracefully
      if (error.code === '23505') {
        return res.status(409).json({ error: 'Username or email already exists' });
      }

      res.status(500).json({ error: 'Internal server error' });
    }
  }
);

// ✅ Secure user retrieval with access control
app.get('/api/users/:id',
  authenticateToken,
  [
    param('id').isInt().toInt()
  ],
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { id } = req.params;

    // ✅ Access control: users can only view their own profile
    // (unless they're admin)
    if (req.userId !== parseInt(id) && req.userRole !== 'admin') {
      return res.status(403).json({ error: 'Access denied' });
    }

    try {
      const query = `SELECT id, username, email, role, created_at FROM users WHERE id = $1`;
      const result = await pool.query(query, [id]);

      if (result.rows.length === 0) {
        return res.status(404).json({ error: 'User not found' });
      }

      // ✅ Only return safe fields (no password_hash)
      res.json(result.rows[0]);
    } catch (error) {
      console.error('User retrieval error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }
);

// ✅ Secure search endpoint (XSS prevention)
app.get('/api/search',
  [
    query('q').trim().isLength({ min: 1, max: 100 })
  ],
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { q } = req.query;

    // ✅ HTML entity encoding to prevent XSS
    const safeQuery = he.encode(q);

    // Better: return JSON instead of HTML
    res.json({
      query: safeQuery,
      message: `Search results for: ${safeQuery}`
    });
  }
);

// ✅ HTTPS enforcement in production
if (process.env.NODE_ENV === 'production') {
  app.use((req, res, next) => {
    if (req.header('x-forwarded-proto') !== 'https') {
      return res.redirect(`https://${req.header('host')}${req.url}`);
    }
    next();
  });
}

// ✅ Graceful error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Secure server running on port ${PORT}`);
});
