# Contributing Template

Use this template as a starting point. Customize it for your specific project.

---

# Contributing to {Project}

Thank you for your interest in contributing to {Project}! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Style Guide](#style-guide)
- [License](#license)

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- {Language} {version} or higher
- {Package Manager} {version}
- {Other tools}
- Git {version}

### Finding Something to Work On

- **Good First Issues**: Look for issues labeled `good first issue`
- **Help Wanted**: Check issues labeled `help wanted`
- **Documentation**: Help improve documentation
- **Tests**: Add or improve test coverage

### Claiming an Issue

1. Find an issue you'd like to work on
2. Comment on the issue to let others know you're working on it
3. Wait for assignment (for maintainers)
4. Start working on the issue

## Development Setup

### 1. Fork the Repository

```bash
# Fork on GitHub, then clone
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
# Sync with upstream
git fetch upstream
git checkout -b {type}/{description} upstream/main

# Examples:
git checkout -b feature/add-oauth
git checkout -b fix/null-pointer
git checkout -b docs/update-readme
```

### 5. Verify Setup

```bash
# Run tests
{test_command}

# Run linter
{lint_command}

# Run formatter
{format_command}
```

## Making Changes

### Branch Naming

Use descriptive branch names:

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/{description}` | `feature/add-oauth` |
| Bug Fix | `fix/{description}` | `fix/null-pointer` |
| Documentation | `docs/{description}` | `docs/update-readme` |
| Refactor | `refactor/{description}` | `refactor/extract-utils` |
| Test | `test/{description}` | `test/add-unit-tests` |

### Coding Standards

Follow the project's coding standards:

- [ ] Code follows the style guide
- [ ] Functions are small and focused
- [ ] Variables are descriptively named
- [ ] Comments explain WHY, not WHAT
- [ ] No console.log statements (use proper logging)
- [ ] Error handling is proper
- [ ] No hardcoded values

### Testing

- Write tests for new features
- Maintain or improve test coverage
- Use descriptive test names
- Test edge cases

```bash
# Run all tests
{test_command}

# Run specific tests
{test_command} {test_file}

# Run with coverage
{coverage_command}
```

### Documentation

- Update README if adding features
- Add JSDoc/TSDoc for new functions
- Update API documentation if applicable
- Add examples for new features

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

### Examples

```
feat(auth): add OAuth2 support

- Implement OAuth2 flow
- Add provider configuration
- Update documentation

Closes #123
```

```
fix(api): handle null response from upstream

The upstream API sometimes returns null instead of an empty array.
This fix normalizes the response before processing.

Fixes #456
```

### Rules

- Use imperative mood ("add feature" not "added feature")
- Keep subject line under 72 characters
- Reference issues when applicable
- Use body for complex changes
- Don't use a period at the end of the subject line

## Pull Request Process

### Before Submitting

1. **Update your branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run all checks**
   ```bash
   {test_command}
   {lint_command}
   {format_command}
   ```

3. **Update documentation**
   - README (if adding features)
   - API docs (if changing API)
   - CHANGELOG (if significant change)

### Submitting

1. Push your branch
   ```bash
   git push origin {branch-name}
   ```

2. Create a pull request on GitHub

3. Fill out the PR template completely:
   - Description of changes
   - Type of change
   - Related issues
   - Testing performed
   - Checklist

4. Add appropriate labels:
   - `bug`, `enhancement`, `documentation`, etc.
   - `priority: high/medium/low`
   - `status: needs review`

5. Request review from maintainers

### Review Process

1. Maintainers will review your PR
2. Address feedback promptly
3. Make requested changes
4. Push updates to the same branch
5. Respond to review comments

### After Merge

1. Delete your feature branch
2. Pull the latest main
3. Update your local repository
4. Celebrate! 🎉

## Reporting Issues

### Bug Reports

When reporting bugs, include:

1. **Description**: Clear description of the bug
2. **Steps to reproduce**: How to reproduce the issue
3. **Expected behavior**: What you expected to happen
4. **Actual behavior**: What actually happened
5. **Environment**: OS, browser, version, etc.
6. **Screenshots**: If applicable

### Feature Requests

When requesting features, include:

1. **Description**: Clear description of the feature
2. **Use case**: Why you need this feature
3. **Alternatives**: Any alternatives you've considered
4. **Additional context**: Any other information

### Security Issues

For security issues, please see [SECURITY.md](SECURITY.md). Do NOT create public issues for security vulnerabilities.

## Style Guide

### Code Style

- Follow the project's coding standards
- Use consistent indentation
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused

### Documentation Style

- Use clear, concise language
- Include code examples
- Use proper markdown formatting
- Link to related documentation

## License

By contributing, you agree that your contributions will be licensed under the [LICENSE](LICENSE).

## Questions?

If you have questions about contributing, feel free to:

- Open a discussion
- Ask in Discord/Slack
- Create an issue with the `question` label

Thank you for contributing to {Project}! 🎉
