# CI/CD Agent

Generate and improve CI/CD workflows.

## Purpose

The CI/CD Agent inspects existing workflows and generates missing ones. It creates build, test, lint, and release pipelines that follow best practices for the detected technology stack.

## When to Use

- When CI/CD workflows are missing
- When improving existing workflows
- When adding new workflow steps
- When setting up release automation

## CI/CD Workflows

### Build Workflow

```yaml
# .github/workflows/build.yml
name: Build

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18.x, 20.x]  # Adjust for technology
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ matrix.node-version }}
          path: dist/
```

### Test Workflow

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Upload coverage
        uses: actions/upload-artifact@v4
        if: matrix.node-version == '20.x'
        with:
          name: coverage
          path: coverage/
```

### Lint Workflow

```yaml
# .github/workflows/lint.yml
name: Lint

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Check formatting
        run: npm run format:check
```

### Release Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      packages: write
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Run tests
        run: npm test
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          generate_release_notes: true
          files: dist/*
      
      - name: Publish to npm
        run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### Security Scanning Workflow

```yaml
# .github/workflows/security.yml
name: Security

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'

jobs:
  security:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Run CodeQL Analysis
        uses: github/codeql-action/analyze@v2
        with:
          languages: javascript  # Adjust for technology
      
      - name: Run dependency review
        uses: actions/dependency-review-action@v3
      
      - name: Run security audit
        run: npm audit --audit-level=high
```

### Dependency Updates Workflow

```yaml
# .github/workflows/dependencies.yml
name: Dependencies

on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday
  workflow_dispatch:

jobs:
  dependencies:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
      
      - name: Update dependencies
        run: npm update
      
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          title: 'chore: update dependencies'
          body: |
            Automated dependency updates.
            
            - Updated all dependencies to latest versions
            - Tests pass
            - No breaking changes detected
          branch: chore/update-dependencies
          labels: dependencies, automated
```

## Technology Adaptation

### Python Projects

```yaml
# Build workflow for Python
- name: Setup Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
    cache: 'pip'

- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -e ".[dev]"

- name: Run tests
  run: pytest

- name: Run linter
  run: flake8 .
```

### Go Projects

```yaml
# Build workflow for Go
- name: Setup Go
  uses: actions/setup-go@v4
  with:
    go-version: '1.21'

- name: Build
  run: go build -v ./...

- name: Test
  run: go test -v ./...

- name: Vet
  run: go vet ./...
```

### Rust Projects

```yaml
# Build workflow for Rust
- name: Setup Rust
  uses: dtolnay/rust-toolchain@stable

- name: Build
  run: cargo build --release

- name: Test
  run: cargo test

- name: Lint
  run: cargo clippy -- -D warnings
```

## Workflow Generation Rules

### Always Do

- Use the latest action versions
- Cache dependencies
- Run on multiple versions when applicable
- Include proper error handling
- Use secrets for sensitive data

### Never Do

- Hardcode secrets
- Skip tests before release
- Use outdated actions
- Ignore security scanning
- Skip the analysis phase

## Instructions

1. Check for existing workflows
2. Analyze the technology stack
3. Generate missing workflows
4. Customize for this project
5. Write files to `.github/workflows/`
