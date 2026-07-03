# Development Template

Use this template as a starting point. Customize it for your specific project.

---

# Development Guide

This guide explains how to set up and work on {Project} for development.

## Prerequisites

Before you begin, ensure you have:

- {Language} {version} or higher
- {Package Manager} {version}
- {Other tools}
- Git {version}
- {IDE} with recommended extensions

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone
git clone https://github.com/{your-username}/{repo}.git
cd {repo}
```

### 2. Add Upstream Remote

```bash
git remote add upstream https://github.com/{owner}/{repo}.git
```

### 3. Install Dependencies

```bash
{install_command}
```

### 4. Set Up Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
```

### 5. Verify Setup

```bash
# Run tests
{test_command}

# Run linter
{lint_command}

# Start development server
{dev_command}
```

## Project Structure

```
{repo}/
├── src/                    # Source code
│   ├── core/              # Core logic
│   ├── api/               # API layer
│   └── utils/             # Utilities
├── tests/                 # Test files
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── docs/                  # Documentation
├── scripts/               # Build scripts
├── .github/               # GitHub configuration
└── {config_files}         # Project configuration
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture.

## Development Workflow

### Creating a Branch

```bash
# Sync with upstream
git fetch upstream

# Create a feature branch
git checkout -b feature/your-feature upstream/main

# Or a bug fix branch
git checkout -b fix/your-bug upstream/main
```

### Making Changes

1. Make your changes
2. Write or update tests
3. Run tests: `{test_command}`
4. Run linter: `{lint_command}`
5. Format code: `{format_command}`
6. Commit your changes

### Committing

Follow the commit convention:

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Submitting a Pull Request

1. Push your branch:
   ```bash
   git push origin feature/your-feature
   ```

2. Create a pull request on GitHub

3. Fill out the PR template

4. Wait for review

## Coding Standards

### General

- Follow {language} conventions
- Write clear, readable code
- Add comments for complex logic
- Keep functions small and focused

### Naming Conventions

- Files: `{naming_convention}`
- Functions: `{naming_convention}`
- Variables: `{naming_convention}`
- Constants: `{naming_convention}`

### Formatting

- Use {formatter} for formatting
- Run `{format_command}` before committing
- Follow the project's `.editorconfig`

### Linting

- Use {linter} for linting
- Run `{lint_command}` to check
- Fix all lint errors before committing

## Testing

### Running Tests

```bash
# Run all tests
{test_command}

# Run specific tests
{test_command} {test_file}

# Run with coverage
{coverage_command}
```

### Writing Tests

- Write tests for new features
- Maintain test coverage
- Use descriptive test names
- Test edge cases

### Test Structure

```{language}
{test_example}
```

## Debugging

### Debug Mode

```bash
{debug_command}
```

### Logging

{Logging patterns for this project}

### Common Issues

1. **Issue**: {common_issue}
   **Solution**: {solution}

2. **Issue**: {common_issue}
   **Solution**: {solution}

3. **Issue**: {common_issue}
   **Solution**: {solution}

## IDE Setup

### VS Code

Recommended extensions:

- {extension1}
- {extension2}
- {extension3}

Settings:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "{formatter}",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

### Other IDEs

{IDE-specific setup instructions}

## Build

### Development Build

```bash
{dev_build_command}
```

### Production Build

```bash
{prod_build_command}
```

### Build Output

The build output is in `{build_output_dir}/`.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions.

## Getting Help

- **Issues**: [{link}]({link})
- **Discussions**: [{link}]({link})
- **Discord**: [{link}]({link})

See [SUPPORT.md](SUPPORT.md) for more options.

---

Thank you for contributing to {Project}! 🎉
