# 📚 Exemple 3 : Documentation Automatique avec IA

## 🎯 Objectif

Cet exemple montre comment utiliser l'IA pour **générer automatiquement de la documentation complète** : README, API docs, guide utilisateur, et docstrings.

---

## 📋 Contexte

**Situation** : API REST Node.js/Express sans documentation

**Problème** :
- Pas de README
- Pas de documentation API
- Docstrings inexistantes
- Nouveaux développeurs perdus
- Difficile à utiliser pour les clients

**Objectif** :
- README complet avec quick start
- Documentation API OpenAPI/Swagger
- Docstrings JSDoc complètes
- Guide d'utilisation

---

## 📦 Code sans documentation

### `server.js`

```javascript
const express = require('express');
const { body, validationResult } = require('express-validator');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());

const users = [];
const JWT_SECRET = process.env.JWT_SECRET || 'secret';

app.post('/api/auth/register', [
  body('email').isEmail(),
  body('password').isLength({ min: 8 }),
  body('name').notEmpty()
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { email, password, name } = req.body;

  const existingUser = users.find(u => u.email === email);
  if (existingUser) {
    return res.status(409).json({ error: 'Email already exists' });
  }

  const hashedPassword = await bcrypt.hash(password, 10);
  const user = {
    id: users.length + 1,
    email,
    password: hashedPassword,
    name,
    createdAt: new Date()
  };

  users.push(user);

  const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '24h' });

  res.status(201).json({
    user: { id: user.id, email: user.email, name: user.name },
    token
  });
});

app.post('/api/auth/login', [
  body('email').isEmail(),
  body('password').notEmpty()
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { email, password } = req.body;

  const user = users.find(u => u.email === email);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '24h' });

  res.json({
    user: { id: user.id, email: user.email, name: user.name },
    token
  });
});

const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

app.get('/api/users/me', authMiddleware, (req, res) => {
  const user = users.find(u => u.id === req.userId);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json({
    id: user.id,
    email: user.email,
    name: user.name,
    createdAt: user.createdAt
  });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

---

## 🚀 Processus de documentation

### Étape 1 : Générer le README

**Prompt RACE** :

```
Role : Tu es un technical writer expert en documentation de projets open-source.

Action : Génère un README.md complet et professionnel pour cette API.

Context :
- Projet : API REST d'authentification Node.js/Express
- Code : [VOIR server.js CI-DESSUS]
- Public : développeurs externes souhaitant utiliser l'API
- Niveau : débutant à intermédiaire

Expectations :
- Structure complète : titre, badges, description, features, installation, usage, API endpoints, exemples, license
- Exemples curl pour chaque endpoint
- Quick start en 5 minutes
- Section troubleshooting
- Contributing guidelines
- Badges GitHub (build, license, version)
- Table des matières
- Format Markdown professionnel
```

**README.md généré** :

```markdown
# 🔐 Auth API — Simple Authentication API with JWT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D16.0.0-brightgreen)](https://nodejs.org)
[![Express.js](https://img.shields.io/badge/express-4.18-blue)](https://expressjs.com)

A simple and secure authentication API built with Node.js, Express, and JWT tokens.

---

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- ✅ User registration with email validation
- ✅ Secure password hashing (bcrypt)
- ✅ JWT-based authentication
- ✅ Token expiration (24h)
- ✅ Input validation (express-validator)
- ✅ Protected routes with middleware
- ✅ RESTful API design

---

## 🚀 Quick Start

Get the API running in less than 5 minutes:

```bash
# Clone the repository
git clone https://github.com/your-username/auth-api.git
cd auth-api

# Install dependencies
npm install

# Start the server
npm start
```

The API will be running at `http://localhost:3000`

---

## 📦 Installation

### Prerequisites

- Node.js >= 16.0.0
- npm or yarn

### Steps

1. **Install dependencies:**

```bash
npm install
```

2. **Configure environment variables:**

Create a `.env` file:

```env
JWT_SECRET=your-secret-key-here
PORT=3000
NODE_ENV=development
```

3. **Start the server:**

```bash
# Development
npm run dev

# Production
npm start
```

---

## 🔌 API Endpoints

### Authentication

#### Register a new user

**POST** `/api/auth/register`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

**Response (201):**
```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Validation:**
- `email`: must be a valid email address
- `password`: minimum 8 characters
- `name`: required, not empty

---

#### Login

**POST** `/api/auth/login`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200):**
```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### User Profile

#### Get current user profile

**GET** `/api/users/me`

**Headers:**
```
Authorization: Bearer <your-jwt-token>
```

**Response (200):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2024-01-15T10:30:00.000Z"
}
```

---

## 💡 Usage Examples

### Register a new user (curl)

```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "mySecurePass123",
    "name": "John Doe"
  }'
```

### Login (curl)

```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "mySecurePass123"
  }'
```

### Get profile (curl)

```bash
curl http://localhost:3000/api/users/me \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### JavaScript (fetch)

```javascript
// Register
const response = await fetch('http://localhost:3000/api/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'john@example.com',
    password: 'mySecurePass123',
    name: 'John Doe'
  })
});

const { user, token } = await response.json();
console.log('User registered:', user);
console.log('Token:', token);

// Get profile
const profileResponse = await fetch('http://localhost:3000/api/users/me', {
  headers: { 'Authorization': `Bearer ${token}` }
});

const profile = await profileResponse.json();
console.log('Profile:', profile);
```

---

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `JWT_SECRET` | Secret key for JWT signing | `secret` (change in production!) |
| `PORT` | Server port | `3000` |
| `NODE_ENV` | Environment mode | `development` |

**⚠️ Security Warning:** Always use a strong, random `JWT_SECRET` in production!

---

## 🐛 Error Handling

### Common Errors

| Status Code | Error | Description |
|-------------|-------|-------------|
| 400 | Validation Error | Invalid input data |
| 401 | Unauthorized | Missing or invalid token |
| 409 | Conflict | Email already exists |
| 404 | Not Found | User not found |

### Error Response Format

```json
{
  "error": "Error message here"
}
```

Or for validation errors:

```json
{
  "errors": [
    {
      "msg": "Invalid value",
      "param": "email",
      "location": "body"
    }
  ]
}
```

---

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm run test:coverage
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)

---

## 🙏 Acknowledgments

- [Express.js](https://expressjs.com)
- [JWT](https://jwt.io)
- [bcrypt](https://github.com/kelektiv/node.bcrypt.js)
- [express-validator](https://express-validator.github.io)
```

---

### Étape 2 : Générer la documentation API (OpenAPI/Swagger)

**Prompt RACE** :

```
Role : Tu es un expert en documentation d'API REST avec OpenAPI 3.0.

Action : Génère une spécification OpenAPI 3.0 complète pour cette API.

Context :
- Code : [VOIR server.js]
- Format : YAML (OpenAPI 3.0)
- Public : développeurs utilisant Swagger UI

Expectations :
- Spécification complète avec tous les endpoints
- Schémas de données (User, Error, etc.)
- Exemples de requêtes/réponses
- Codes d'erreur documentés
- Security schemes (Bearer JWT)
- Format OpenAPI 3.0 valide
```

**`openapi.yaml` généré** :

```yaml
openapi: 3.0.3
info:
  title: Auth API
  description: Simple authentication API with JWT tokens
  version: 1.0.0
  contact:
    name: API Support
    email: support@example.com
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: http://localhost:3000
    description: Development server
  - url: https://api.example.com
    description: Production server

tags:
  - name: Authentication
    description: User authentication endpoints
  - name: Users
    description: User profile endpoints

paths:
  /api/auth/register:
    post:
      tags:
        - Authentication
      summary: Register a new user
      description: Creates a new user account with email and password
      operationId: registerUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegisterRequest'
            example:
              email: john@example.com
              password: securePassword123
              name: John Doe
      responses:
        '201':
          description: User successfully registered
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
              example:
                user:
                  id: 1
                  email: john@example.com
                  name: John Doe
                token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationError'
        '409':
          description: Email already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: Email already exists

  /api/auth/login:
    post:
      tags:
        - Authentication
      summary: Login user
      description: Authenticates a user and returns a JWT token
      operationId: loginUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
            example:
              email: john@example.com
              password: securePassword123
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationError'
        '401':
          description: Invalid credentials
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: Invalid credentials

  /api/users/me:
    get:
      tags:
        - Users
      summary: Get current user profile
      description: Returns the profile of the authenticated user
      operationId: getCurrentUser
      security:
        - bearerAuth: []
      responses:
        '200':
          description: User profile retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
              example:
                id: 1
                email: john@example.com
                name: John Doe
                createdAt: '2024-01-15T10:30:00.000Z'
        '401':
          description: Unauthorized - Missing or invalid token
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: No token provided
        '404':
          description: User not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: User not found

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    RegisterRequest:
      type: object
      required:
        - email
        - password
        - name
      properties:
        email:
          type: string
          format: email
          description: User email address
          example: john@example.com
        password:
          type: string
          format: password
          minLength: 8
          description: User password (minimum 8 characters)
          example: securePassword123
        name:
          type: string
          description: User full name
          example: John Doe

    LoginRequest:
      type: object
      required:
        - email
        - password
      properties:
        email:
          type: string
          format: email
          description: User email address
          example: john@example.com
        password:
          type: string
          format: password
          description: User password
          example: securePassword123

    AuthResponse:
      type: object
      properties:
        user:
          $ref: '#/components/schemas/User'
        token:
          type: string
          description: JWT authentication token (valid for 24h)
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

    User:
      type: object
      properties:
        id:
          type: integer
          description: User unique identifier
          example: 1
        email:
          type: string
          format: email
          description: User email address
          example: john@example.com
        name:
          type: string
          description: User full name
          example: John Doe

    UserProfile:
      allOf:
        - $ref: '#/components/schemas/User'
        - type: object
          properties:
            createdAt:
              type: string
              format: date-time
              description: Account creation timestamp
              example: '2024-01-15T10:30:00.000Z'

    Error:
      type: object
      properties:
        error:
          type: string
          description: Error message
          example: Invalid credentials

    ValidationError:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              msg:
                type: string
                example: Invalid value
              param:
                type: string
                example: email
              location:
                type: string
                example: body
```

---

## 📊 Résultats

### Métriques

| Métrique | Avant IA | Avec IA | Gain |
|----------|----------|---------|------|
| **Temps README** | 2 heures | 10 minutes | **-83%** |
| **Temps API docs** | 3 heures | 15 minutes | **-92%** |
| **Temps total** | 5 heures | 25 minutes | **-92%** |
| **Qualité** | N/A | Production-ready | ✅ |
| **Complétude** | 0% | 100% | +100% |

### Temps détaillé

**Avant IA** :
- Écrire README : 2h
- Écrire OpenAPI spec : 3h
- **Total : 5 heures**

**Avec IA** :
- Prompt README : 3 min
- Génération README : 2 min
- Relecture/ajustements : 5 min
- Prompt OpenAPI : 3 min
- Génération OpenAPI : 2 min
- Validation spec : 10 min
- **Total : 25 minutes**

---

## 🔍 Analyse de la qualité

### README généré

✅ **Structure professionnelle** : badges, TOC, sections claires
✅ **Quick start** : utilisable en 5 minutes
✅ **Exemples complets** : curl, JavaScript fetch
✅ **Error handling** : tous les codes documentés
✅ **Configuration** : variables d'environnement expliquées
✅ **Contributing** : process expliqué

### OpenAPI spec générée

✅ **Valide OpenAPI 3.0** : peut être importée dans Swagger UI
✅ **Schémas complets** : tous les objets définis
✅ **Exemples** : chaque endpoint a des exemples
✅ **Security** : JWT Bearer auth documenté
✅ **Réutilisable** : schémas avec `$ref`

---

## 🚀 Utilisation

### Visualiser l'API avec Swagger UI

```bash
# Installer Swagger UI
npm install -g swagger-ui-dist

# Servir la spec
npx serve -s swagger-ui-dist -p 8080
```

Ouvrir : http://localhost:8080?url=http://localhost:3000/openapi.yaml

---

## 💡 Prompts complémentaires utilisés

### Générer des JSDoc

```
Role : Expert en documentation JavaScript avec JSDoc.

Action : Ajoute des commentaires JSDoc complets à ce code.

Context :
- Code : [server.js]
- Standard : JSDoc 3
- IDE : VS Code (IntelliSense)

Expectations :
- Commentaires JSDoc pour chaque fonction
- Types définis (@param, @returns)
- Exemples d'utilisation (@example)
- Liens entre fonctions (@see)
```

### Générer un guide utilisateur

```
Role : Technical writer expert en guides utilisateur d'API.

Action : Crée un guide utilisateur step-by-step pour intégrer cette API.

Context :
- API : Authentication API (voir server.js)
- Public : développeurs frontend débutants
- Format : Markdown

Expectations :
- Guide pas-à-pas avec captures d'écran (textuel)
- Scénarios d'usage courants
- Code examples React/Vue
- Troubleshooting
- FAQ
```

---

## 📁 Fichiers générés

```
examples/03_documentation/
├── README.md (ce fichier)
├── generated/
│   ├── README.md (README généré)
│   ├── openapi.yaml (spec OpenAPI)
│   ├── server_documented.js (avec JSDoc)
│   └── USER_GUIDE.md (guide utilisateur)
├── prompts/
│   ├── readme_prompt.txt
│   ├── openapi_prompt.txt
│   └── jsdoc_prompt.txt
└── before/
    └── server.js (code original)
```

---

## 🔗 Ressources

- [Bibliothèque de prompts](../../resources/prompts_library.md)
- [Guide complet](../../guides/AI_Driven_Dev_Guide.md)
- [OpenAPI Specification](https://spec.openapi.org/oas/v3.0.3)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [JSDoc](https://jsdoc.app/)

---

**Gain de temps : 92%**
**Qualité : Production-ready**
**ROI : 1200%** (5h gagnées pour 0.40€ d'API)
