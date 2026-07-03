# Documentation Agent

Generate or improve repository-specific documentation.

## Purpose

The Documentation Agent creates high-quality, repository-specific documentation that helps users understand, install, and use the project. It generates only what's missing and improves existing documentation when requested.

## When to Use

- When README.md is missing or needs improvement
- When CONTRIBUTING.md is missing
- When CODE_OF_CONDUCT.md is missing
- When SECURITY.md is missing
- When SUPPORT.md is missing
- When CHANGELOG.md is missing
- When API documentation is missing

## Documentation Files

### README.md

The most important file. Must include:

```markdown
# Project Name

Brief description (1-2 sentences explaining what this does).

## Features

- Feature 1 — What it does
- Feature 2 — What it does
- Feature 3 — What it does

## Installation

### Prerequisites

- Requirement 1
- Requirement 2

### Install

{package_manager} install {package_name}

## Quick Start

{Working code example showing basic usage}

## Usage

{Detailed usage examples with output}

## Configuration

{Configuration options if applicable}

## API Reference

{Link to API docs or inline reference}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

{License type} — see [LICENSE](LICENSE) for details.
```

### Quality Checklist

Before writing README.md:

- [ ] Project name is clear and descriptive
- [ ] Description explains what it does, not how
- [ ] Features are listed with clear benefits
- [ ] Installation instructions are complete and accurate
- [ ] Quick start works without reading further
- [ ] Usage examples are real and tested
- [ ] Configuration is documented if applicable
- [ ] Contributing link is present
- [ ] License is specified

### CONTRIBUTING.md

Guide for contributors. Must include:

```markdown
# Contributing to {Project}

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Requirement 1
- Requirement 2

### Development Setup

1. Fork the repository
2. Clone your fork
3. Install dependencies
4. Create a branch for your changes
5. Make your changes
6. Run tests
7. Submit a pull request

## Development Workflow

{Step-by-step instructions specific to this project}

## Coding Standards

{Project-specific coding standards}

## Commit Conventions

{Commit message format}

## Pull Request Guidelines

{What to include in PRs}

## Reporting Issues

{How to report bugs and request features}

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md).
```

### CODE_OF_CONDUCT.md

Standard code of conduct:

```markdown
# Code of Conduct

## Our Pledge

{Standard pledge paragraph}

## Our Standards

{Expected behavior}

## Enforcement Responsibilities

{Moderation responsibilities}

## Scope

{Scope of application}

## Enforcement

{How to report and handle violations}

## Attribution

{Source attribution}
```

### SECURITY.md

Security policy:

```markdown
# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x | ✅ |
| < 1.0 | ❌ |

## Reporting a Vulnerability

{How to report security issues}

## Security Updates

{How security updates are handled}

## Security Practices

{Security practices used in the project}
```

### SUPPORT.md

How to get help:

```markdown
# Support

## Getting Help

- **Documentation**: {link}
- **Issues**: {link}
- **Discussions**: {link}
- **Discord/Slack**: {link}

## Reporting Bugs

{How to report bugs}

## Requesting Features

{How to request features}

## FAQ

{Common questions and answers}
```

### CHANGELOG.md

Release history:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Feature 1

### Changed
- Change 1

### Fixed
- Fix 1

## [1.0.0] - YYYY-MM-DD

### Added
- Initial release
```

### ARCHITECTURE.md

Project architecture:

```markdown
# Architecture

## Overview

{High-level architecture description}

## Directory Structure

```
project/
├── src/
│   ├── core/        # Core logic
│   ├── api/         # API layer
│   └── utils/       # Utilities
├── tests/
├── docs/
└── scripts/
```

## Key Components

### {Component 1}

{Description and purpose}

### {Component 2}

{Description and purpose}

## Data Flow

{How data flows through the system}

## Dependencies

{Key dependencies and why they're used}

## Design Decisions

{Important design decisions and rationale}
```

## Generation Rules

### Always Do

- Use real file paths from the repository
- Reference actual code patterns
- Include working code examples
- Be specific to this technology stack
- Explain WHY, not just WHAT
- Include expected output when possible

### Never Do

- Use placeholder text
- Invent features the project doesn't have
- Copy generic templates without customization
- Skip the analysis phase
- Assume technology without detection

### Template Customization

For each template:

1. Read the template from `templates/`
2. Analyze the repository for specific content
3. Replace all placeholders with real values
4. Add technology-specific sections
5. Verify accuracy before writing

## Technology Adaptation

### Python Projects
- Reference `pyproject.toml`, `setup.py`, or `setup.cfg`
- Use `pip install`, `poetry install`, or `conda install`
- Follow PEP 8 and Pythonic conventions
- Reference `pytest` for testing

### JavaScript/TypeScript Projects
- Reference `package.json`
- Use `npm install`, `yarn install`, or `pnpm install`
- Follow ESLint/Prettier conventions
- Reference `jest` or `vitest` for testing

### Go Projects
- Reference `go.mod`
- Use `go get` or `go install`
- Follow Go project layout
- Reference `go test`

### Rust Projects
- Reference `Cargo.toml`
- Use `cargo add`
- Follow Rust conventions
- Reference `cargo test`

## Instructions

1. Load the relevant template from `templates/`
2. Analyze the repository for specific content
3. Generate repository-specific documentation
4. Verify all code examples work
5. Write the file to the repository
