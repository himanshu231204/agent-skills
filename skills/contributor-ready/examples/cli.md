# CLI Project Example

This example demonstrates how to use contributor-ready with a CLI tool project.

## Project Structure

```
my-cli-project/
├── src/
│   ├── commands/
│   │   ├── init.ts
│   │   ├── build.ts
│   │   └── serve.ts
│   ├── utils/
│   │   ├── logger.ts
│   │   └── config.ts
│   ├── index.ts
│   └── cli.ts
├── tests/
│   ├── commands/
│   │   ├── init.test.ts
│   │   ├── build.test.ts
│   │   └── serve.test.ts
│   └── utils/
│       └── logger.test.ts
├── docs/
│   └── commands.md
├── bin/
│   └── my-cli
├── package.json
├── tsconfig.json
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a CLI project, contributor-ready detects:

- **Type**: CLI tool (by bin field in package.json)
- **Language**: TypeScript or JavaScript (by file extensions)
- **Package Manager**: npm, yarn, or pnpm (by lock files)
- **CLI Framework**: Commander, Yargs, oroclif (by dependencies)
- **Testing**: Jest or Vitest (by config files)

## Generated Files

### README.md

```markdown
# my-cli

A command-line tool for {description}.

## Installation

### From npm

```bash
npm install -g my-cli
```

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
npm install
npm link
```

## Usage

### Basic Usage

```bash
# Initialize a new project
my-cli init

# Build the project
my-cli build

# Start development server
my-cli serve
```

### Commands

| Command | Description |
|---------|-------------|
| `my-cli init` | Initialize a new project |
| `my-cli build` | Build the project |
| `my-cli serve` | Start development server |
| `my-cli help` | Show help |

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-v, --verbose` | Enable verbose logging | `false` |
| `-o, --output <dir>` | Output directory | `./dist` |
| `-c, --config <path>` | Config file path | `./my-cli.config.js` |

## Examples

### Initialize a Project

```bash
my-cli init my-project
```

Output:

```
✓ Created project directory
✓ Initialized package.json
✓ Created configuration file
✓ Project ready!

Get started:
  cd my-project
  my-cli serve
```

### Build a Project

```bash
my-cli build --output ./build
```

Output:

```
✓ Reading configuration
✓ Compiling sources
✓ Writing output
✓ Build complete!

Output: ./build
```

### Start Development Server

```bash
my-cli serve --port 3000
```

Output:

```
✓ Starting server on port 3000
✓ Watching for changes

Server running at http://localhost:3000
Press Ctrl+C to stop
```

## Configuration

### Configuration File

Create a `my-cli.config.js` file:

```javascript
module.exports = {
  // Build options
  build: {
    output: './dist',
    target: 'es2020',
    minify: true,
  },
  
  // Server options
  server: {
    port: 3000,
    host: 'localhost',
    open: true,
  },
  
  // Plugin options
  plugins: [],
};
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MY_CLI_DEBUG` | Enable debug mode | `false` |
| `MY_CLI_CONFIG` | Config file path | `./my-cli.config.js` |

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/{owner}/{repo}.git
cd {repo}

# Install dependencies
npm install

# Link for local development
npm link
```

### Commands

```bash
# Build
npm run build

# Watch mode
npm run dev

# Test
npm test

# Lint
npm run lint

# Format
npm run format
```

### Project Structure

```
src/
├── commands/      # CLI commands
├── utils/         # Utility functions
├── index.ts       # Entry point
└── cli.ts         # CLI setup
```

## Testing

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

### Test Structure

```typescript
import { initCommand } from '../commands/init';

describe('init command', () => {
  it('creates a new project', async () => {
    const result = await initCommand('my-project');
    expect(result.success).toBe(true);
  });
});
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### package.json

```json
{
  "name": "my-cli",
  "version": "0.1.0",
  "description": "A command-line tool for {description}",
  "main": "dist/index.js",
  "bin": {
    "my-cli": "./bin/my-cli"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "test:watch": "vitest --watch",
    "lint": "eslint src/ --ext .ts",
    "lint:fix": "eslint src/ --ext .ts --fix",
    "format": "prettier --write \"src/**/*.ts\"",
    "format:check": "prettier --check \"src/**/*.ts\"",
    "type-check": "tsc --noEmit",
    "prepublishOnly": "npm run build"
  },
  "keywords": [
    "cli",
    "command-line",
    "tool"
  ],
  "author": "{author}",
  "license": "MIT",
  "dependencies": {
    "commander": "^11.1.0",
    "chalk": "^5.3.0",
    "ora": "^7.0.1",
    "inquirer": "^9.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "eslint": "^8.55.0",
    "prettier": "^3.1.0",
    "typescript": "^5.3.0",
    "vitest": "^1.1.0"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### bin/my-cli

```bash
#!/usr/bin/env node

const { program } = require('commander');
const { version } = require('../package.json');

program
  .name('my-cli')
  .description('A command-line tool for {description}')
  .version(version);

program
  .command('init [project-name]')
  .description('Initialize a new project')
  .action((name) => {
    require('../dist/commands/init').initCommand(name);
  });

program
  .command('build')
  .description('Build the project')
  .option('-o, --output <dir>', 'Output directory', './dist')
  .action((options) => {
    require('../dist/commands/build').buildCommand(options);
  });

program
  .command('serve')
  .description('Start development server')
  .option('-p, --port <port>', 'Port number', '3000')
  .option('-h, --host <host>', 'Host name', 'localhost')
  .action((options) => {
    require('../dist/commands/serve').serveCommand(options);
  });

program.parse();
```

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: ['18', '20']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Format check
        run: npm run format:check
      
      - name: Type check
        run: npm run type-check
      
      - name: Test
        run: npm run test:coverage
      
      - name: Build
        run: npm run build
      
      - name: Test CLI
        run: |
          npm link
          my-cli --help
          my-cli init test-project
          ls test-project
```

## Checklist

When using contributor-ready with a CLI project:

- [ ] Detect CLI framework
- [ ] Detect bin entry point
- [ ] Check for command documentation
- [ ] Check for help text
- [ ] Check for version info
- [ ] Generate CLI-specific README
- [ ] Generate CLI-specific CONTRIBUTING.md
- [ ] Generate CLI-specific CI workflow
- [ ] Generate CLI-specific SECURITY.md
- [ ] Generate command documentation
