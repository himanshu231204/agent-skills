---
name: oss-ready
description: "Transform any repository into a professional, contributor-friendly open source project. Analyzes repo health, generates documentation, creates GitHub community files, identifies contribution opportunities, and produces a readiness report. Agent-independent and technology-agnostic."
---

# oss-ready

**Open Source Maintainer Assistant** — Analyze, document, and prepare any repository for open source contribution.

## What This Does

This skill transforms software repositories into professional, contributor-friendly open source projects. It does NOT generate generic templates — it analyzes your actual codebase and produces repository-specific artifacts.

### Core Capabilities

- **Repository Analysis** — Detect language, framework, architecture, maturity, and readiness gaps
- **Documentation Generation** — Create README, CONTRIBUTING, SECURITY, and all essential docs
- **GitHub Community** — Issue templates, PR templates, CODEOWNERS, label strategy
- **Contribution Opportunities** — Identify real, meaningful issues from code analysis
- **Architecture Mapping** — Document structure, dependencies, and module relationships
- **CI/CD Workflows** — Generate build, test, lint, and release pipelines
- **Developer Experience** — Setup guides, coding standards, commit conventions
- **Release Management** — Versioning strategy, changelogs, release checklists
- **Readiness Report** — Scored assessment across all dimensions

## When to Use

- Preparing a repository for public open source release
- Onboarding new contributors to an existing project
- Auditing repository health and community readiness
- Generating missing documentation for an existing project
- Creating contribution opportunities from code analysis
- Establishing CI/CD pipelines for open source projects

## Commands

| Command | Description |
|---------|-------------|
| `oss-ready audit` | Analyze repository and generate readiness report |
| `oss-ready generate` | Generate all missing documentation and community files |
| `oss-ready improve` | Improve existing documentation without rewrites |
| `oss-ready issues` | Create meaningful contribution opportunities |
| `oss-ready full` | Run complete pipeline: audit → generate → report |

## Quick Start

### Full Pipeline

```
Run oss-ready on this repository to make it contributor-ready.
```

### Audit Only

```
Run oss-ready audit on this repository. Generate a readiness report without making changes.
```

### Generate Missing

```
Run oss-ready generate. Create only the files that are missing from this repository.
```

### Improve Existing

```
Run oss-ready improve. Enhance existing documentation without rewrites.
```

## Workflow

### Phase 1: Repository Analysis

The skill always starts by analyzing the repository:

1. **Detect project type** — Application, library, CLI tool, API, monorepo
2. **Detect languages** — Primary and secondary languages with percentages
3. **Detect frameworks** — React, Next.js, FastAPI, Django, Spring Boot, etc.
4. **Detect package managers** — npm, pip, cargo, go mod, maven, etc.
5. **Detect build systems** — webpack, vite, make, cargo, etc.
6. **Detect testing setup** — pytest, jest, vitest, go test, etc.
7. **Detect CI/CD** — GitHub Actions, GitLab CI, CircleCI, etc.
8. **Detect existing documentation** — README, CONTRIBUTING, etc.
9. **Detect GitHub configuration** — Issue templates, PR templates, etc.
10. **Assess maturity** — Commit history, contributor count, release tags

### Phase 2: Readiness Assessment

Generate a readiness report with scores:

| Dimension | Score | Weight |
|-----------|-------|--------|
| Documentation | 0-100 | 25% |
| GitHub Community | 0-100 | 20% |
| CI/CD | 0-100 | 15% |
| Testing | 0-100 | 15% |
| Developer Experience | 0-100 | 15% |
| Security | 0-100 | 10% |

**Overall Score**: Weighted average

### Phase 3: Artifact Generation

Based on the audit, generate missing artifacts:

- Documentation files
- GitHub community files
- Contribution opportunities
- CI/CD workflows
- Developer experience guides
- Release management docs

### Phase 4: Report

Produce a final report with:

- Readiness scores
- Prioritized recommendations
- Generated artifacts list
- Next steps

## Safe Mode

This skill operates in safe mode by default:

- **Never** overwrites existing files unless explicitly requested
- **Never** generates generic placeholder content
- **Never** makes assumptions without repository analysis
- **Always** improves existing documentation when possible
- **Always** produces repository-specific content
- **Always** explains what was generated and why

To regenerate a file that already exists, explicitly request it:

```
Regenerate the README.md for this repository.
```

## Agent Independence

This skill works with any AI coding agent:

- Claude Code / Opencode
- Cursor / Codex CLI
- Gemini CLI / Cline
- Aider / Continue
- Any agent that follows Markdown instructions

The agents directory contains modular instruction files that any agent can follow.

## Technology Support

Works with repositories built using:

**Languages**: Python, JavaScript, TypeScript, Go, Rust, Java, C#, C++, PHP, Ruby, Swift, Kotlin

**Frameworks**: React, Next.js, Vue, Angular, Express, FastAPI, Django, Flask, Spring Boot, NestJS, Rails, Laravel, Svelte, Astro

**Platforms**: Node.js, Deno, Bun, .NET, JVM, WASM

**Tools**: CLI applications, browser extensions, mobile apps, desktop apps, libraries, SDKs, monorepos

## Architecture

```
oss-ready/
├── skill.md              # This file — entry point and usage guide
├── AGENT.md              # Orchestration instructions for agents
├── prompt.md             # System prompt for the skill
├── agents/               # Specialized agent instructions
│   ├── audit.md          # Repository analysis
│   ├── docs.md           # Documentation generation
│   ├── github.md         # GitHub community files
│   ├── issues.md         # Contribution opportunities
│   ├── architecture.md   # Architecture mapping
│   ├── roadmap.md        # Roadmap generation
│   ├── ci.md             # CI/CD workflows
│   ├── devex.md          # Developer experience
│   ├── release.md        # Release management
│   └── report.md         # Readiness report
├── templates/            # Reusable documentation templates
│   ├── README.md
│   ├── CONTRIBUTING.md
│   ├── CODE_OF_CONDUCT.md
│   ├── SECURITY.md
│   ├── SUPPORT.md
│   ├── ROADMAP.md
│   ├── CHANGELOG.md
│   ├── DEVELOPMENT.md
│   ├── ARCHITECTURE.md
│   ├── ISSUE_TEMPLATE.md
│   └── PR_TEMPLATE.md
├── examples/             # Technology-specific guides
│   ├── python.md
│   ├── fastapi.md
│   ├── react.md
│   ├── nextjs.md
│   ├── cli.md
│   ├── library.md
│   └── chrome-extension.md
└── checklist.md          # Comprehensive readiness checklist
```

## Related Skills

- `opensource-pipeline` — Fork, sanitize, and package private projects for public release
- `security-review` — Security checklist for new projects
- `coding-standards` — Baseline coding conventions
- `repo-scan` — Repository audit and asset classification

## License

MIT
