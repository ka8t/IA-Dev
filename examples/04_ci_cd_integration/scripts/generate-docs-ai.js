#!/usr/bin/env node

/**
 * Auto-generate API documentation using OpenAI
 */

const fs = require('fs');
const path = require('path');
const OpenAI = require('openai');

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function generateAPIDocs() {
  // Find all API route files
  const routesDir = path.join(__dirname, '../backend/routes');

  // Create routes directory if it doesn't exist (for example purposes)
  if (!fs.existsSync(routesDir)) {
    console.log('⚠️  Routes directory not found. Creating example documentation...');

    const exampleDocs = `# API Documentation

Auto-generated documentation.

## Example Routes

This is a placeholder documentation file. In a real project, this would be generated from your actual route files.

### Authentication Endpoints

#### POST /api/auth/register
- **Description**: Register a new user
- **Body**: \`{ email: string, password: string, name: string }\`
- **Response**: \`{ user: Object, token: string }\`

#### POST /api/auth/login
- **Description**: Login user
- **Body**: \`{ email: string, password: string }\`
- **Response**: \`{ user: Object, token: string }\`

### User Endpoints

#### GET /api/users/me
- **Description**: Get current user profile
- **Headers**: \`Authorization: Bearer <token>\`
- **Response**: \`{ id: number, email: string, name: string, createdAt: string }\`

---

*Generated automatically by AI documentation system*
`;

    const docsPath = path.join(__dirname, '../docs/API.md');
    fs.mkdirSync(path.dirname(docsPath), { recursive: true });
    fs.writeFileSync(docsPath, exampleDocs);
    console.log('✅ Example API documentation generated: docs/API.md');
    return;
  }

  const routeFiles = fs.readdirSync(routesDir)
    .filter(f => f.endsWith('.js'));

  let fullDocs = '# API Documentation\n\nAuto-generated documentation.\n\n';

  for (const file of routeFiles) {
    const filePath = path.join(routesDir, file);
    const code = fs.readFileSync(filePath, 'utf8');

    const prompt = `
Role: You are a technical writer expert in API documentation.

Action: Generate Markdown documentation for this Express route file.

Context:
- File: ${file}
- Code:
\`\`\`javascript
${code}
\`\`\`

Expectations:
- List all endpoints with HTTP methods
- Parameters (query, body, path)
- Response formats
- Error codes
- Example requests (curl)
- Keep it concise and clear
`;

    try {
      const response = await openai.chat.completions.create({
        model: 'gpt-4-turbo-preview',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.2
      });

      const docs = response.choices[0].message.content;
      fullDocs += `\n## ${file}\n\n${docs}\n\n---\n\n`;
    } catch (error) {
      console.error(`Error documenting ${file}:`, error.message);
    }
  }

  // Write documentation
  const docsPath = path.join(__dirname, '../docs/API.md');
  fs.mkdirSync(path.dirname(docsPath), { recursive: true });
  fs.writeFileSync(docsPath, fullDocs);

  console.log('✅ API documentation generated: docs/API.md');
}

generateAPIDocs().catch(error => {
  console.error('Error:', error);
  process.exit(1);
});
