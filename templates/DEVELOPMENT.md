# Development Guide

This guide explains how to set up and work on {Project} for development.

## Prerequisites

Before you begin, ensure you have:

- {Language} {version} or higher
- {Package Manager} {version}
- Git

## Getting Started

### 1. Fork and Clone

```bash
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
cp .env.example .env
# Edit .env with your settings
```

### 5. Verify Setup

```bash
{test_command}
{lint_command}
{dev_command}
```

## Project Structure

```
{repo}/
├── src/                    # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── scripts/                # Build scripts
├── .github/                # GitHub configuration
└── {config_files}          # Project configuration
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture.

## Development Workflow

### Creating a Branch

```bash
git fetch upstream
git checkout -b feature/your-feature upstream/main
```

### Making Changes

1. Make your changes
2. Write or update tests
3. Run tests: `{test_command}`
4. Run linter: `{lint_command}`
5. Commit your changes

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

1. Push your branch
2. Create a pull request on GitHub
3. Fill out the PR template
4. Wait for review

## Coding Standards

### General

- Follow {language} conventions
- Write clear, readable code
- Add comments for complex logic
- Keep functions small and focused

### Formatting

- Use {formatter} for formatting
- Run `{format_command}` before committing

### Linting

- Use {linter} for linting
- Run `{lint_command}` to check
- Fix all lint errors before committing

## Testing

```bash
# Run all tests
{test_command}

# Run specific tests
{test_command} {test_file}
```

## Debugging

### Common Issues

1. **Issue**: {common_issue}
   **Solution**: {solution}

2. **Issue**: {common_issue}
   **Solution**: {solution}

## IDE Setup

### VS Code

Recommended extensions:
- {extension1}
- {extension2}

Settings:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "{formatter}"
}
```

## Getting Help

- **Issues**: [{issues_link}]({issues_link})
- **Discussions**: [{discussions_link}]({discussions_link})

See [SUPPORT.md](SUPPORT.md) for more options.
