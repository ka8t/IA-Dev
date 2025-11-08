#!/usr/bin/env node

/**
 * AI Documentation Generator
 *
 * Automatically generates API documentation using OpenAI GPT-4.
 *
 * Usage:
 *   node scripts/generate_docs_ai.js
 *   node scripts/generate_docs_ai.js --dir src/routes
 *   node scripts/generate_docs_ai.js --file src/api/users.js
 *
 * Environment variables:
 *   OPENAI_API_KEY: OpenAI API key (required)
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Check for OpenAI package
let OpenAI;
try {
  OpenAI = require('openai');
} catch (error) {
  console.error('❌ Error: openai package not installed');
  console.error('Install with: npm install openai');
  process.exit(1);
}

// Configuration
const CONFIG = {
  apiKey: process.env.OPENAI_API_KEY,
  model: 'gpt-4-turbo-preview',
  temperature: 0.2,
  defaultDir: 'src',
  outputDir: 'docs',
  codeExtensions: ['.js', '.ts', '.jsx', '.tsx', '.py', '.go', '.java']
};

/**
 * Validate environment
 */
function validateEnvironment() {
  if (!CONFIG.apiKey) {
    console.error('❌ Error: OPENAI_API_KEY environment variable not set');
    process.exit(1);
  }
}

/**
 * Find code files recursively
 */
function findCodeFiles(dir) {
  const files = [];

  function walk(directory) {
    const entries = fs.readdirSync(directory, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(directory, entry.name);

      // Skip node_modules, .git, etc.
      if (entry.isDirectory()) {
        if (!['node_modules', '.git', 'dist', 'build', '__pycache__'].includes(entry.name)) {
          walk(fullPath);
        }
      } else {
        // Check if it's a code file
        const ext = path.extname(entry.name);
        if (CONFIG.codeExtensions.includes(ext)) {
          files.push(fullPath);
        }
      }
    }
  }

  walk(dir);
  return files;
}

/**
 * Generate documentation for a file using AI
 */
async function generateDocumentation(filePath, openai) {
  try {
    // Read file content
    const code = fs.readFileSync(filePath, 'utf8');

    // Prepare prompt
    const prompt = `
Role: You are a technical writer expert in API documentation.

Action: Generate comprehensive Markdown documentation for this code file.

Context:
- File: ${filePath}
- Code:
\`\`\`
${code}
\`\`\`

Expectations:
- Clear description of what this file does
- List all exported functions/classes/endpoints
- Parameters and return types
- Usage examples
- Error handling
- Keep it concise and well-structured
- Use Markdown format

If this is an API route file, include:
- HTTP method and endpoint
- Request parameters (query, body, path)
- Response format
- Status codes
- Example requests (curl)
`;

    // Call OpenAI API
    const response = await openai.chat.completions.create({
      model: CONFIG.model,
      messages: [{ role: 'user', content: prompt }],
      temperature: CONFIG.temperature
    });

    const documentation = response.choices[0].message.content;

    return {
      file: filePath,
      documentation,
      success: true
    };

  } catch (error) {
    console.error(`❌ Error generating docs for ${filePath}:`, error.message);
    return {
      file: filePath,
      documentation: null,
      success: false,
      error: error.message
    };
  }
}

/**
 * Generate index file for all documentation
 */
function generateIndex(results, outputDir) {
  const lines = [
    '# API Documentation',
    '',
    'Auto-generated documentation for the codebase.',
    '',
    '## 📋 Table of Contents',
    ''
  ];

  // Group by directory
  const byDirectory = {};

  for (const result of results) {
    if (!result.success) continue;

    const dir = path.dirname(result.file);
    if (!byDirectory[dir]) {
      byDirectory[dir] = [];
    }
    byDirectory[dir].push(result);
  }

  // Generate TOC
  for (const [dir, files] of Object.entries(byDirectory).sort()) {
    lines.push(`### ${dir}`);
    lines.push('');

    for (const result of files) {
      const filename = path.basename(result.file);
      const docFilename = filename.replace(path.extname(filename), '.md');
      const relativePath = path.relative(outputDir, path.join(outputDir, dir, docFilename));

      lines.push(`- [${filename}](${relativePath})`);
    }

    lines.push('');
  }

  // Footer
  lines.push('---');
  lines.push('');
  lines.push(`*Generated on ${new Date().toISOString()}*`);
  lines.push('');
  lines.push('*Powered by GPT-4*');

  return lines.join('\n');
}

/**
 * Main function
 */
async function main() {
  // Parse arguments
  const args = process.argv.slice(2);
  let targetDir = CONFIG.defaultDir;
  let targetFile = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--dir' && args[i + 1]) {
      targetDir = args[i + 1];
      i++;
    } else if (args[i] === '--file' && args[i + 1]) {
      targetFile = args[i + 1];
      i++;
    } else if (args[i] === '--help') {
      console.log(`
Usage: node scripts/generate_docs_ai.js [OPTIONS]

Options:
  --dir DIR      Directory to scan for code files (default: src)
  --file FILE    Specific file to document
  --help         Show this help message

Environment variables:
  OPENAI_API_KEY: OpenAI API key (required)

Examples:
  node scripts/generate_docs_ai.js
  node scripts/generate_docs_ai.js --dir src/routes
  node scripts/generate_docs_ai.js --file src/api/users.js
      `);
      process.exit(0);
    }
  }

  // Validate environment
  validateEnvironment();

  // Initialize OpenAI client
  const openai = new OpenAI({ apiKey: CONFIG.apiKey });

  console.log('🤖 AI Documentation Generator\n');

  // Get files to document
  let files;
  if (targetFile) {
    if (!fs.existsSync(targetFile)) {
      console.error(`❌ File not found: ${targetFile}`);
      process.exit(1);
    }
    files = [targetFile];
  } else {
    if (!fs.existsSync(targetDir)) {
      console.error(`❌ Directory not found: ${targetDir}`);
      process.exit(1);
    }
    files = findCodeFiles(targetDir);
  }

  if (files.length === 0) {
    console.log('⚠️  No code files found');
    process.exit(0);
  }

  console.log(`Found ${files.length} file(s) to document\n`);

  // Create output directory
  fs.mkdirSync(CONFIG.outputDir, { recursive: true });

  // Generate documentation for each file
  const results = [];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const progress = `[${i + 1}/${files.length}]`;

    console.log(`${progress} Documenting: ${file}`);

    const result = await generateDocumentation(file, openai);
    results.push(result);

    if (result.success) {
      // Save documentation
      const relativePath = path.relative(targetDir, file);
      const docPath = path.join(
        CONFIG.outputDir,
        relativePath.replace(path.extname(file), '.md')
      );

      // Create subdirectories if needed
      fs.mkdirSync(path.dirname(docPath), { recursive: true });

      // Write documentation
      fs.writeFileSync(docPath, result.documentation);

      console.log(`  ✅ Saved to: ${docPath}`);
    } else {
      console.log(`  ❌ Failed: ${result.error}`);
    }
  }

  console.log('');

  // Generate index
  const index = generateIndex(results, CONFIG.outputDir);
  const indexPath = path.join(CONFIG.outputDir, 'API.md');
  fs.writeFileSync(indexPath, index);

  console.log(`📄 Generated index: ${indexPath}\n`);

  // Summary
  const successCount = results.filter(r => r.success).length;
  const failCount = results.filter(r => !r.success).length;

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅ Documentation generation complete!');
  console.log('');
  console.log(`Success: ${successCount}`);
  console.log(`Failed:  ${failCount}`);
  console.log(`Total:   ${files.length}`);
  console.log('');
  console.log(`Output directory: ${CONFIG.outputDir}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
}

// Run main function
main().catch(error => {
  console.error('❌ Fatal error:', error);
  process.exit(1);
});
