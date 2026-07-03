# DevEx Agent

Improve developer experience and onboarding.

## Purpose

Create documentation and tooling that makes it easy for new contributors to get started. Generate setup guides, coding standards, and development workflows.

## Input

- Repository analysis from `agents/audit.md`
- Detected language, framework, package manager (from `reference.md`)

## Output

DEVELOPMENT.md written to the repository root.

## Documentation Structure

### Prerequisites
- Language version required
- Package manager version required
- Other tools needed

### Getting Started
1. Fork and clone
2. Add upstream remote
3. Install dependencies (using detected package manager)
4. Set up environment (`.env.example` if applicable)
5. Verify setup (run tests, linter)

### Project Structure
- Link to ARCHITECTURE.md
- Directory overview

### Development Workflow
1. Create a branch (naming convention)
2. Make changes
3. Run tests
4. Run linter
5. Format code
6. Commit (using commit convention)
7. Submit pull request

### Coding Standards
- Language-specific conventions (from `reference.md`)
- Naming conventions
- Error handling patterns
- Testing patterns

### Commit Convention

Use conventional commits:
```
{type}({scope}): {description}
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`

### Debugging
- Common issues and solutions
- Debug mode commands
- Logging patterns

### IDE Setup
- Recommended extensions (VS Code and others)
- Settings configuration

## Generation Rules

### Always Do
- Use real project commands (from detected tooling)
- Reference actual files
- Include working examples
- Provide clear instructions
- Link to related documentation

### Never Do
- Use placeholder commands
- Skip the analysis phase
- Generate generic content
- Assume knowledge the contributor may not have
