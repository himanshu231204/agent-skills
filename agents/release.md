# Release Agent

Generate release management documentation.

## Purpose

The Release Agent creates documentation for versioning, changelogs, and release processes. It helps maintainers manage releases consistently and professionally.

## When to Use

- When setting up release processes
- When creating CHANGELOG.md
- When documenting versioning strategy
- When automating releases

## Release Documentation

### Semantic Versioning

```markdown
# Versioning Strategy

This project follows [Semantic Versioning](https://semver.org/).

## Version Format

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## When to Increment

### MAJOR Version

Increment when you make incompatible API changes:

- Remove a public API
- Change function signatures
- Change return types
- Remove configuration options
- Drop support for a version

### MINOR Version

Increment when you add functionality in a backward-compatible manner:

- Add new features
- Add new API endpoints
- Add new configuration options
- Add new exports
- Add new CLI options

### PATCH Version

Increment when you make backward-compatible bug fixes:

- Fix bugs
- Fix security vulnerabilities
- Improve performance (non-breaking)
- Update documentation
- Update dependencies (non-breaking)

## Pre-release Versions

Use pre-release tags for development:

- `1.0.0-alpha.1` — Early development
- `1.0.0-beta.1` — Feature complete, testing
- `1.0.0-rc.1` — Release candidate

## Examples

```
1.0.0 → 1.0.1  (bug fix)
1.0.0 → 1.1.0  (new feature)
1.0.0 → 2.0.0  (breaking change)
1.0.0 → 1.1.0-alpha.1  (pre-release)
```
```

### CHANGELOG.md

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Feature 1
- Feature 2

### Changed
- Change 1
- Change 2

### Deprecated
- Deprecation 1

### Removed
- Removal 1

### Fixed
- Fix 1
- Fix 2

### Security
- Security fix 1

## [1.2.0] - YYYY-MM-DD

### Added
- Feature 1
- Feature 2

### Fixed
- Fix 1

## [1.1.0] - YYYY-MM-DD

### Added
- Feature 1

### Changed
- Change 1

## [1.0.0] - YYYY-MM-DD

### Added
- Initial release
- Feature 1
- Feature 2
- Feature 3

[Unreleased]: https://github.com/{owner}/{repo}/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/{owner}/{repo}/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/{owner}/{repo}/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/{owner}/{repo}/releases/tag/v1.0.0
```

### Release Checklist

```markdown
# Release Checklist

## Pre-release

- [ ] All tests pass
- [ ] Linter passes
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in package.json
- [ ] No breaking changes (or documented)

## Release

- [ ] Create release branch
- [ ] Update version
- [ ] Update CHANGELOG.md
- [ ] Commit changes
- [ ] Create tag
- [ ] Push to GitHub
- [ ] Create GitHub Release
- [ ] Publish to package manager

## Post-release

- [ ] Verify release is published
- [ ] Update documentation
- [ ] Announce release
- [ ] Close milestone
- [ ] Clean up release branch
```

### Release Workflow

```markdown
# Release Workflow

## Manual Release

### 1. Update Version

```bash
# Update version in package.json
npm version {major|minor|patch}
```

### 2. Update Changelog

Add entries to CHANGELOG.md:
- New features
- Bug fixes
- Breaking changes

### 3. Commit Changes

```bash
git add .
git commit -m "chore: release v{version}"
```

### 4. Create Tag

```bash
git tag v{version}
```

### 5. Push

```bash
git push origin main --tags
```

### 6. Create GitHub Release

1. Go to GitHub Releases
2. Create new release from tag
3. Add release notes
4. Publish

## Automated Release

Releases are automated via GitHub Actions:

1. Push a tag matching `v*`
2. GitHub Actions will:
   - Build the project
   - Run tests
   - Create GitHub Release
   - Publish to package manager

## Hotfix Release

For critical bug fixes:

1. Create hotfix branch from main
2. Fix the bug
3. Update CHANGELOG.md
4. Bump patch version
5. Create tag
6. Follow release workflow
```

### Changelog Strategy

```markdown
# Changelog Strategy

## What to Include

### Added
- New features
- New API endpoints
- New configuration options
- New exports

### Changed
- Changes to existing features
- Changes to API
- Changes to behavior
- Changes to configuration

### Deprecated
- Features that will be removed
- API that will change
- Configuration that will change

### Removed
- Removed features
- Removed API
- Removed configuration

### Fixed
- Bug fixes
- Security fixes
- Performance improvements

### Security
- Security vulnerability fixes
- Security improvements

## What NOT to Include

- Internal refactoring (unless user-facing)
- Documentation changes (unless significant)
- Dependency updates (unless breaking)
- Build system changes (unless user-facing)

## Linking to Issues

Reference issues in changelog:

```
### Fixed
- Handle null response from upstream API ([#123](https://github.com/{owner}/{repo}/issues/123))
```

## Linking to PRs

Reference pull requests:

```
### Added
- OAuth2 support ([#456](https://github.com/{owner}/{repo}/pull/456))
```
```

## Generation Rules

### Always Do

- Use semantic versioning
- Maintain a complete changelog
- Document breaking changes
- Provide clear release notes
- Follow existing patterns

### Never Do

- Skip version bumps
- Forget to update changelog
- Ignore breaking changes
- Rush releases without testing

## Instructions

1. Analyze the repository's release history
2. Detect existing versioning patterns
3. Generate semantic versioning documentation
4. Create CHANGELOG.md structure
5. Document release workflow
6. Write release documentation
