# Release Agent

Generate release management documentation.

## Purpose

Create documentation for versioning, changelogs, and release processes. Help maintainers manage releases consistently and professionally.

## Input

- Repository analysis from `agents/audit.md`
- Detected package manager (from `reference.md`)
- Release history from git tags

## Output

- CHANGELOG.md (if missing)
- Release documentation in docs/ (if applicable)
- Versioning strategy documentation

## Documentation to Generate

### Semantic Versioning

Document the versioning strategy following [Semantic Versioning](https://semver.org/):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)
- Pre-release tags: alpha, beta, rc

### CHANGELOG.md (from `templates/CHANGELOG.md`)

Follow [Keep a Changelog](https://keepachangelog.com/) format:
- [Unreleased] section with Added, Changed, Deprecated, Removed, Fixed, Security
- Versioned sections with date
- Links to GitHub comparisons

### Release Checklist

- Pre-release: tests pass, lint passes, docs updated, CHANGELOG updated, version bumped
- Release: create branch, update version, commit, tag, push, create release, publish
- Post-release: verify, update docs, announce, close milestone

### Release Workflow

Document both manual and automated release processes:
- Manual: version bump, changelog update, commit, tag, push
- Automated: push tag → CI builds, tests, creates release, publishes

## Generation Rules

### Always Do
- Use semantic versioning
- Maintain a complete changelog
- Document breaking changes
- Provide clear release notes
- Follow existing patterns in the repository

### Never Do
- Skip version bumps
- Forget to update changelog
- Ignore breaking changes
- Rush releases without testing
- Assume npm when the project uses a different package manager
