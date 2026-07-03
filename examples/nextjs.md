# Next.js Project Example

This example demonstrates how to use oss-ready with a Next.js project.

## Project Structure

```
my-nextjs-project/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── about/
│   │   └── page.tsx
│   ├── blog/
│   │   ├── page.tsx
│   │   └── [slug]/
│   │       └── page.tsx
│   └── api/
│       └── users/
│           └── route.ts
├── components/
│   ├── Header.tsx
│   ├── Footer.tsx
│   └── Button.tsx
├── lib/
│   ├── utils.ts
│   └── api.ts
├── public/
│   ├── images/
│   └── favicon.ico
├── styles/
│   └── globals.css
├── tests/
│   ├── components/
│   └── pages/
├── docs/
│   └── deployment.md
├── package.json
├── next.config.js
├── tsconfig.json
├── tailwind.config.js
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a Next.js project, oss-ready detects:

- **Framework**: Next.js (by `next` in package.json)
- **Language**: TypeScript or JavaScript (by file extensions)
- **Package Manager**: npm, yarn, or pnpm (by lock files)
- **Styling**: Tailwind CSS, CSS Modules, or styled-components
- **Testing**: Jest, Vitest, or Playwright
- **Deployment**: Vercel, Netlify, or self-hosted

## Generated Files

### README.md

```markdown
# My Next.js Project

A Next.js application for {description}.

## Features

- **App Router** — Built with Next.js 14+ App Router
- **Server Components** — React Server Components for performance
- **Type Safety** — Full TypeScript support
- **Styling** — Tailwind CSS for styling
- **Testing** — Comprehensive test suite

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

# Start production server
npm start
```

## Usage

### Development

```bash
npm run dev
```

Open http://localhost:3000 in your browser.

### Production Build

```bash
npm run build
npm start
```

## Project Structure

```
app/              # App Router pages and layouts
├── layout.tsx    # Root layout
├── page.tsx      # Home page
└── about/        # About page
components/       # Reusable UI components
lib/              # Utility functions and API clients
public/           # Static assets
styles/           # Global styles
tests/            # Test files
```

## Pages

### Home Page (`/`)

The landing page with hero section and features.

### About Page (`/about`)

About page with company information.

### Blog Pages (`/blog`)

Dynamic blog pages with markdown support.

## API Routes

### Users API (`/api/users`)

| Method | Description |
|--------|-------------|
| GET | List all users |
| POST | Create a user |

## Components

### Button

```tsx
import { Button } from '@/components/Button';

<Button variant="primary" size="large">
  Click Me
</Button>
```

### Header

```tsx
import { Header } from '@/components/Header';

<Header
  title="My App"
  links={[
    { label: 'Home', href: '/' },
    { label: 'About', href: '/about' },
  ]}
/>
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | API base URL | `http://localhost:3000` |
| `DATABASE_URL` | Database connection string | (required) |

### Configuration File

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:3000
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Styling

### Tailwind CSS

This project uses Tailwind CSS for styling.

```tsx
<div className="bg-blue-500 text-white p-4 rounded-lg">
  Styled with Tailwind
</div>
```

### CSS Modules

```tsx
import styles from './Button.module.css';

<button className={styles.primary}>Click Me</button>
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
import { render, screen } from '@testing-library/react';
import { Button } from '@/components/Button';

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });
});
```

## Deployment

### Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Self-Hosted

```bash
# Build
npm run build

# Start
npm start
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['localhost'],
  },
};

module.exports = nextConfig;
```

### tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './lib/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0070f3',
      },
    },
  },
  plugins: [],
};
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
      
      - name: Type check
        run: npm run type-check
      
      - name: Test
        run: npm run test:coverage
      
      - name: Build
        run: npm run build
```

## Checklist

When using oss-ready with a Next.js project:

- [ ] Detect Next.js framework
- [ ] Detect App Router usage
- [ ] Detect styling solution
- [ ] Detect deployment target
- [ ] Check for API routes
- [ ] Check for server components
- [ ] Generate Next.js-specific README
- [ ] Generate Next.js-specific CONTRIBUTING.md
- [ ] Generate Next.js-specific CI workflow
- [ ] Generate Next.js-specific SECURITY.md
