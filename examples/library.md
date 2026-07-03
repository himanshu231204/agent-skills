# Library Project Example

This example demonstrates how to use oss-ready with a library project.

## Project Structure

```
my-library/
├── src/
│   ├── index.ts
│   ├── utils.ts
│   ├── types.ts
│   └── constants.ts
├── tests/
│   ├── utils.test.ts
│   └── integration.test.ts
├── docs/
│   ├── api.md
│   └── examples.md
├── examples/
│   ├── basic-usage.ts
│   └── advanced-usage.ts
├── package.json
├── tsconfig.json
├── tsconfig.build.json
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a library project, oss-ready detects:

- **Type**: Library (by no bin field, exports in package.json)
- **Language**: TypeScript or JavaScript (by file extensions)
- **Package Manager**: npm, yarn, or pnpm (by lock files)
- **Build System**: TypeScript, Rollup, or esbuild
- **Testing**: Jest or Vitest
- **Documentation**: TypeDoc or JSDoc

## Generated Files

### README.md

```markdown
# my-library

A TypeScript library for {description}.

## Installation

### From npm

```bash
npm install my-library
```

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
npm install
npm run build
```

## Quick Start

```typescript
import { doSomething, formatDate } from 'my-library';

// Basic usage
const result = doSomething('input');
console.log(result);

// With options
const formatted = formatDate(new Date(), { format: 'YYYY-MM-DD' });
console.log(formatted);
```

## Features

- **Type Safe** — Full TypeScript support
- **Tree Shakable** — Only import what you use
- **Zero Dependencies** — No external dependencies
- **Lightweight** — Small bundle size

## API Reference

### `doSomething(input: string, options?: Options): string`

Process input data.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `string` | Input data to process |
| `options` | `Options` | Optional configuration |

**Options:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `verbose` | `boolean` | `false` | Enable verbose output |
| `format` | `string` | `'default'` | Output format |

**Returns:**

| Type | Description |
|------|-------------|
| `string` | Processed result |

**Example:**

```typescript
import { doSomething } from 'my-library';

const result = doSomething('hello');
// Output: "processed: hello"

const resultWithFormat = doSomething('hello', { format: 'upper' });
// Output: "PROCESSED: HELLO"
```

### `formatDate(date: Date, options?: DateFormatOptions): string`

Format a date.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `date` | `Date` | Date to format |
| `options` | `DateFormatOptions` | Optional formatting options |

**DateFormatOptions:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `format` | `string` | `'YYYY-MM-DD'` | Date format |
| `locale` | `string` | `'en-US'` | Locale |

**Returns:**

| Type | Description |
|------|-------------|
| `string` | Formatted date string |

**Example:**

```typescript
import { formatDate } from 'my-library';

const formatted = formatDate(new Date());
// Output: "2024-01-15"

const formattedWithLocale = formatDate(new Date(), { locale: 'de-DE' });
// Output: "15.01.2024"
```

### `validateInput(input: unknown): ValidationResult`

Validate input data.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `unknown` | Input to validate |

**Returns:**

| Type | Description |
|------|-------------|
| `ValidationResult` | Validation result with success and errors |

**Example:**

```typescript
import { validateInput } from 'my-library';

const result = validateInput('hello');
console.log(result);
// Output: { success: true, errors: [] }

const resultWithError = validateInput('');
console.log(resultWithError);
// Output: { success: false, errors: ['Input cannot be empty'] }
```

## Types

### `Options`

```typescript
interface Options {
  verbose?: boolean;
  format?: 'default' | 'upper' | 'lower';
}
```

### `DateFormatOptions`

```typescript
interface DateFormatOptions {
  format?: string;
  locale?: string;
}
```

### `ValidationResult`

```typescript
interface ValidationResult {
  success: boolean;
  errors: string[];
}
```

## Examples

### Basic Usage

```typescript
import { doSomething, formatDate, validateInput } from 'my-library';

// Process data
const processed = doSomething('hello');
console.log(processed);

// Format date
const formatted = formatDate(new Date());
console.log(formatted);

// Validate input
const validation = validateInput('hello');
if (validation.success) {
  console.log('Input is valid');
}
```

### Advanced Usage

```typescript
import { doSomething, formatDate, Options } from 'my-library';

// Custom options
const options: Options = {
  verbose: true,
  format: 'upper',
};

const result = doSomething('hello', options);
console.log(result);

// With error handling
try {
  const validation = validateInput('');
  if (!validation.success) {
    throw new Error(validation.errors.join(', '));
  }
} catch (error) {
  console.error('Validation failed:', error);
}
```

### React Integration

```tsx
import { useState } from 'react';
import { doSomething } from 'my-library';

function MyComponent() {
  const [result, setResult] = useState('');
  
  const handleClick = () => {
    const processed = doSomething('input');
    setResult(processed);
  };
  
  return (
    <div>
      <button onClick={handleClick}>Process</button>
      <p>Result: {result}</p>
    </div>
  );
}
```

## Configuration

### TypeScript Configuration

This library uses TypeScript with strict mode enabled.

```json
{
  "compilerOptions": {
    "strict": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src"
  }
}
```

### Build Configuration

```json
{
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
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
import { doSomething, validateInput } from '../src';

describe('doSomething', () => {
  it('processes input correctly', () => {
    const result = doSomething('hello');
    expect(result).toBe('processed: hello');
  });
  
  it('handles options', () => {
    const result = doSomething('hello', { format: 'upper' });
    expect(result).toBe('PROCESSED: HELLO');
  });
});

describe('validateInput', () => {
  it('validates correct input', () => {
    const result = validateInput('hello');
    expect(result.success).toBe(true);
  });
  
  it('rejects empty input', () => {
    const result = validateInput('');
    expect(result.success).toBe(false);
  });
});
```

## Publishing

### Build

```bash
npm run build
```

### Test

```bash
npm test
npm run lint
npm run format:check
```

### Publish

```bash
npm publish
```

### Versioning

Follow semantic versioning:

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### package.json

```json
{
  "name": "my-library",
  "version": "0.1.0",
  "description": "A TypeScript library for {description}",
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  },
  "files": [
    "dist",
    "README.md"
  ],
  "scripts": {
    "build": "tsc && rollup -c",
    "dev": "tsc --watch",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "test:watch": "vitest --watch",
    "lint": "eslint src/ --ext .ts",
    "lint:fix": "eslint src/ --ext .ts --fix",
    "format": "prettier --write \"src/**/*.ts\"",
    "format:check": "prettier --check \"src/**/*.ts\"",
    "type-check": "tsc --noEmit",
    "docs": "typedoc src/index.ts",
    "prepublishOnly": "npm run build"
  },
  "keywords": [
    "library",
    "typescript",
    "utility"
  ],
  "author": "{author}",
  "license": "MIT",
  "devDependencies": {
    "@types/node": "^20.10.0",
    "eslint": "^8.55.0",
    "prettier": "^3.1.0",
    "rollup": "^4.9.0",
    "rollup-plugin-typescript2": "^0.36.0",
    "typedoc": "^0.25.0",
    "typescript": "^5.3.0",
    "vitest": "^1.1.0"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### tsconfig.build.json

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./dist",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src"],
  "exclude": ["tests", "examples"]
}
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
      
      - name: Generate docs
        run: npm run docs
```

## Checklist

When using oss-ready with a library project:

- [ ] Detect library type
- [ ] Detect TypeScript usage
- [ ] Check for proper exports
- [ ] Check for type definitions
- [ ] Check for API documentation
- [ ] Check for examples
- [ ] Generate library-specific README
- [ ] Generate library-specific CONTRIBUTING.md
- [ ] Generate library-specific CI workflow
- [ ] Generate library-specific SECURITY.md
- [ ] Generate API documentation
- [ ] Generate usage examples
