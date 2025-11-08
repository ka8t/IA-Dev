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
