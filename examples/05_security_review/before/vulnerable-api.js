const express = require('express');
const { Pool } = require('pg');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

// ❌ VULNÉRABILITÉ : Secret hardcodé
const JWT_SECRET = 'mysecret123';

// ❌ VULNÉRABILITÉ : Credentials en clair
const pool = new Pool({
  user: 'admin',
  password: 'admin123',
  host: 'localhost',
  database: 'mydb'
});

// ❌ VULNÉRABILITÉ : Pas de rate limiting
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;

  // ❌ VULNÉRABILITÉ : SQL Injection
  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

  try {
    const result = await pool.query(query);

    if (result.rows.length > 0) {
      const user = result.rows[0];

      // ❌ VULNÉRABILITÉ : JWT sans expiration
      const token = jwt.sign({ userId: user.id }, JWT_SECRET);

      // ❌ VULNÉRABILITÉ : Expose sensitive data
      res.json({
        token,
        user: user  // Contient password hash !
      });
    } else {
      // ❌ VULNÉRABILITÉ : Information leakage
      res.status(401).json({ error: 'Invalid username or password' });
    }
  } catch (error) {
    // ❌ VULNÉRABILITÉ : Expose stack trace
    res.status(500).json({ error: error.stack });
  }
});

// ❌ VULNÉRABILITÉ : Pas de validation input
app.post('/api/users', async (req, res) => {
  const { username, email, role } = req.body;

  // ❌ VULNÉRABILITÉ : Mass assignment (role peut être admin)
  const query = `INSERT INTO users (username, email, role) VALUES ($1, $2, $3) RETURNING *`;

  try {
    const result = await pool.query(query, [username, email, role]);
    res.status(201).json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ❌ VULNÉRABILITÉ : IDOR (Insecure Direct Object Reference)
app.get('/api/users/:id', async (req, res) => {
  const { id } = req.params;

  // Pas de vérification que l'utilisateur peut accéder à cette ressource
  const query = `SELECT * FROM users WHERE id = $1`;
  const result = await pool.query(query, [id]);

  if (result.rows.length > 0) {
    // ❌ VULNÉRABILITÉ : Expose sensitive data
    res.json(result.rows[0]);
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

// ❌ VULNÉRABILITÉ : XSS possible
app.get('/api/search', async (req, res) => {
  const { q } = req.query;

  // Renvoie la query directement sans sanitization
  res.send(`<h1>Search results for: ${q}</h1>`);
});

// ❌ VULNÉRABILITÉ : Pas de CORS configuration
// ❌ VULNÉRABILITÉ : Pas de helmet (security headers)
// ❌ VULNÉRABILITÉ : Pas de HTTPS enforcement

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
