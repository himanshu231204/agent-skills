# Contributing to {Project}

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- {Language} {version} or higher
- {Package Manager} {version}
- Git

### Finding Something to Work On

- **Good First Issues**: Look for issues labeled `good first issue`
- **Help Wanted**: Check issues labeled `help wanted`
- **Documentation**: Help improve documentation
- **Tests**: Add or improve test coverage

## Development Setup

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

### 4. Create a Branch

```bash
git fetch upstream
git checkout -b {type}/{description} upstream/main
```

### 5. Verify Setup

```bash
{test_command}
{lint_command}
```

## Making Changes

### Branch Naming

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/{description}` | `feature/add-oauth` |
| Bug Fix | `fix/{description}` | `fix/null-pointer` |
| Documentation | `docs/{description}` | `docs/update-readme` |
| Refactor | `refactor/{description}` | `refactor/extract-utils` |
| Test | `test/{description}` | `test/add-unit-tests` |

### Coding Standards

- Follow the project's coding standards
- Write clear, readable code
- Add comments for complex logic
- Keep functions small and focused
- No hardcoded values

### Testing

- Write tests for new features
- Maintain or improve test coverage
- Use descriptive test names
- Test edge cases

```bash
{test_command}
```

## Commit Guidelines

### Commit Message Format

```
{type}({scope}): {description}

{optional body}

{optional footer}
```

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix | `fix(api): handle null response` |
| `docs` | Documentation | `docs(readme): add installation steps` |
| `style` | Formatting | `style: fix indentation` |
| `refactor` | Code refactoring | `refactor(utils): extract helpers` |
| `test` | Tests | `test(auth): add login tests` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance | `perf(query): add caching` |
| `ci` | CI/CD | `ci: add release workflow` |
| `build` | Build | `build: configure webpack` |

### Rules

- Use imperative mood ("add feature" not "added feature")
- Keep subject line under 72 characters
- Reference issues when applicable
- Use body for complex changes
- Do not use a period at the end of the subject line

## Pull Request Process

### Before Submitting

1. Update your branch:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Run all checks:
   ```bash
   {test_command}
   {lint_command}
   ```

3. Update documentation if needed

### Submitting

1. Push your branch
2. Create a pull request on GitHub
3. Fill out the PR template completely
4. Add appropriate labels
5. Request review from maintainers

### Review Process

1. Maintainers will review your PR
2. Address feedback promptly
3. Make requested changes
4. Push updates to the same branch

### After Merge

1. Delete your feature branch
2. Pull the latest main

## Reporting Issues

### Bug Reports

When reporting bugs, include:
1. Clear description of the bug
2. Steps to reproduce
3. Expected vs actual behavior
4. Environment details
5. Screenshots (if applicable)

### Feature Requests

When requesting features, include:
1. Clear description of the feature
2. Use case
3. Alternatives considered
4. Additional context

### Security Issues

For security issues, see [SECURITY.md](SECURITY.md). Do not create public issues for security vulnerabilities.

## License

By contributing, you agree that your contributions will be licensed under the [LICENSE](LICENSE).

## Questions?

If you have questions about contributing, feel free to open a discussion or create an issue with the `question` label.

Thank you for contributing to {Project}!
