# React Project Example

This example demonstrates how to use contributor-ready with a React project.

## Project Structure

```
my-react-project/
├── src/
│   ├── components/
│   │   ├── Header/
│   │   │   ├── Header.tsx
│   │   │   ├── Header.test.tsx
│   │   │   └── Header.module.css
│   │   ├── Footer/
│   │   │   ├── Footer.tsx
│   │   │   ├── Footer.test.tsx
│   │   │   └── Footer.module.css
│   │   └── Button/
│   │       ├── Button.tsx
│   │       ├── Button.test.tsx
│   │       └── Button.module.css
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   └── useApi.ts
│   ├── pages/
│   │   ├── Home/
│   │   │   ├── Home.tsx
│   │   │   └── Home.test.tsx
│   │   └── About/
│   │       ├── About.tsx
│   │       └── About.test.tsx
│   ├── services/
│   │   └── api.ts
│   ├── utils/
│   │   └── helpers.ts
│   ├── types/
│   │   └── index.ts
│   ├── App.tsx
│   ├── App.test.tsx
│   └── main.tsx
├── public/
│   └── index.html
├── tests/
│   └── setup.ts
├── docs/
│   └── components.md
├── package.json
├── tsconfig.json
├── vite.config.ts
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a React project, contributor-ready detects:

- **Framework**: React (by `react` in package.json)
- **Language**: TypeScript or JavaScript (by file extensions)
- **Package Manager**: npm, yarn, or pnpm (by lock files)
- **Build Tool**: Vite, webpack, or create-react-app (by config files)
- **Test Framework**: Jest, Vitest, or React Testing Library (by config files)
- **Linter**: ESLint (by config files)
- **Formatter**: Prettier (by config files)

## Generated Files

### README.md

```markdown
# My React Project

A React application for {description}.

## Features

- **Modern** — Built with React 18 and TypeScript
- **Fast** — Vite for instant HMR
- **Tested** — Comprehensive test suite
- **Accessible** — WCAG 2.1 compliant

## Installation

### Prerequisites

- Node.js 18 or higher
- npm, yarn, or pnpm

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
npm install
```

## Quick Start

```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Usage

### Development

```bash
npm run dev
```

Open http://localhost:5173 in your browser.

### Production Build

```bash
npm run build
npm run preview
```

## Project Structure

```
src/
├── components/     # Reusable UI components
├── hooks/         # Custom React hooks
├── pages/         # Page components
├── services/      # API services
├── utils/         # Utility functions
├── types/         # TypeScript types
├── App.tsx        # Root component
└── main.tsx       # Entry point
```

## Components

### Button

A reusable button component.

```tsx
import { Button } from './components/Button';

function App() {
  return (
    <Button
      variant="primary"
      size="large"
      onClick={() => console.log('Clicked!')}
    >
      Click Me
    </Button>
  );
}
```

**Props:**

| Prop | Type | Description |
|------|------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'danger'` | Button variant |
| `size` | `'small' \| 'medium' \| 'large'` | Button size |
| `onClick` | `() => void` | Click handler |
| `disabled` | `boolean` | Disable the button |
| `children` | `ReactNode` | Button content |

### Header

The application header with navigation.

```tsx
import { Header } from './components/Header';

function App() {
  return (
    <Header
      title="My App"
      links={[
        { label: 'Home', href: '/' },
        { label: 'About', href: '/about' },
      ]}
    />
  );
}
```

## Hooks

### useAuth

Authentication hook.

```tsx
import { useAuth } from './hooks/useAuth';

function App() {
  const { user, login, logout, isAuthenticated } = useAuth();
  
  return (
    <div>
      {isAuthenticated ? (
        <div>
          <p>Welcome, {user.name}!</p>
          <button onClick={logout}>Logout</button>
        </div>
      ) : (
        <button onClick={() => login('email', 'password')}>Login</button>
      )}
    </div>
  );
}
```

### useApi

API fetching hook.

```tsx
import { useApi } from './hooks/useApi';

function App() {
  const { data, loading, error } = useApi('/api/users');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <ul>
      {data.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_URL` | API base URL | `http://localhost:3000` |
| `VITE_APP_TITLE` | Application title | `My App` |

### Configuration File

Create a `.env` file:

```env
VITE_API_URL=http://localhost:3000
VITE_APP_TITLE=My App
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

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });
  
  it('calls onClick when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
```

## Build

### Development Build

```bash
npm run dev
```

### Production Build

```bash
npm run build
```

### Build Output

The build output is in `dist/`.

## Deployment

### Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Netlify

```bash
# Install Netlify CLI
npm i -g netlify-cli

# Deploy
netlify deploy --prod
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### CONTRIBUTING.md

```markdown
# Contributing to My React Project

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Node.js 18 or higher
- npm, yarn, or pnpm

### Development Setup

1. Fork the repository
2. Clone your fork
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start development server:
   ```bash
   npm run dev
   ```

### Making Changes

1. Create a branch for your changes
2. Make your changes
3. Run tests:
   ```bash
   npm test
   ```
4. Run linter:
   ```bash
   npm run lint
   ```
5. Format code:
   ```bash
   npm run format
   ```
6. Commit your changes

### Commit Convention

```
{type}({scope}): {description}
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

### Submitting a Pull Request

1. Push your branch
2. Create a pull request
3. Fill out the PR template
4. Wait for review

## Code Style

- Use TypeScript
- Use functional components with hooks
- Use CSS Modules for styling
- Follow React best practices

## Testing

- Write tests for new features
- Maintain test coverage
- Use React Testing Library
- Use descriptive test names

## Component Guidelines

- Keep components small and focused
- Use proper prop types
- Add JSDoc comments
- Make components accessible

## Questions?

If you have questions, feel free to:

- Open a discussion
- Ask in Discord
- Create an issue with the `question` label
```

### package.json

```json
{
  "name": "my-react-project",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "test:watch": "vitest --watch",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "lint:fix": "eslint . --ext ts,tsx --fix",
    "format": "prettier --write \"src/**/*.{ts,tsx,css}\"",
    "format:check": "prettier --check \"src/**/*.{ts,tsx,css}\"",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.0"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^6.1.0",
    "@testing-library/react": "^14.1.0",
    "@testing-library/user-event": "^14.5.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "@vitejs/plugin-react": "^4.2.0",
    "eslint": "^8.55.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "jsdom": "^23.0.0",
    "prettier": "^3.1.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "vitest": "^1.1.0"
  }
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
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
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
```

## Checklist

When using contributor-ready with a React project:

- [ ] Detect React framework
- [ ] Detect TypeScript usage
- [ ] Detect package manager
- [ ] Detect build tool (Vite, webpack, etc.)
- [ ] Detect testing framework
- [ ] Detect linter (ESLint)
- [ ] Detect formatter (Prettier)
- [ ] Check for component documentation
- [ ] Check for proper prop types
- [ ] Generate React-specific README
- [ ] Generate React-specific CONTRIBUTING.md
- [ ] Generate React-specific CI workflow
- [ ] Generate React-specific SECURITY.md
- [ ] Generate component documentation
