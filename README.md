# oss-ready

[![skills.sh](https://skills.sh/b/himanshu231204/oss-ready)](https://skills.sh/himanshu231204/oss-ready)

An AI skill that transforms any repository into a professional, contributor-friendly open source project. It analyzes your actual codebase and produces repository-specific artifacts — not generic templates.

## What It Does

| Capability | Description |
|------------|-------------|
| Repository Analysis | Detect language, framework, architecture, maturity, and readiness gaps |
| Documentation Generation | Create README, CONTRIBUTING, SECURITY, and all essential docs |
| GitHub Community | Issue templates, PR templates, CODEOWNERS, label strategy |
| Contribution Opportunities | Identify real, meaningful issues from code analysis |
| Architecture Mapping | Document structure, dependencies, and module relationships |
| CI/CD Workflows | Generate build, test, lint, and release pipelines |
| Developer Experience | Setup guides, coding standards, commit conventions |
| Release Management | Versioning strategy, changelogs, release checklists |
| Readiness Report | Scored assessment across six dimensions |

## Quick Start

```
Run oss-ready on this repository to make it contributor-ready.
```

### Commands

| Command | What It Does |
|---------|--------------|
| `oss-ready audit` | Analyze repository, produce readiness report (no file changes) |
| `oss-ready generate` | Create only the files that are missing |
| `oss-ready improve` | Enhance existing documentation in place |
| `oss-ready issues` | Identify real contribution opportunities from code analysis |
| `oss-ready full` | Audit, generate, issues, report — complete pipeline |

## How It Works

1. **Analyze** — Detect project type, languages, frameworks, tooling, and current open source readiness
2. **Score** — Rate six dimensions using weighted scoring
3. **Generate** — Create missing artifacts using templates and repository-specific content
4. **Report** — Produce a readiness report with scores, generated artifacts, and prioritized next steps

## Readiness Dimensions

| Dimension | Weight | What It Checks |
|-----------|--------|----------------|
| Documentation | 25% | README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, CHANGELOG, LICENSE |
| GitHub Community | 20% | Issue templates, PR template, CODEOWNERS, labels, discussions |
| CI/CD | 15% | Build, test, lint, and release workflows |
| Testing | 15% | Test framework, test files, CI integration, coverage |
| Developer Experience | 15% | Setup instructions, development guide, coding standards, commit conventions |
| Security | 10% | SECURITY.md, dependency scanning, secret scanning |

## Technology Support

### Languages

Python, JavaScript, TypeScript, Go, Rust, Java, C#, C++, PHP, Ruby, Swift, Kotlin, Dart, Elixir, Scala, Haskell, Zig, Lua, R

### Frameworks

React, Next.js, Vue, Angular, Svelte, Nuxt, Astro, Remix, Express, NestJS, Fastify, Koa, FastAPI, Django, Flask, Sanic, Spring Boot, Quarkus, Laravel, Rails, Sinatra, Gin, Echo, Fiber, Actix Web, Axum, Rocket, Flutter, Electron, React Native

### Project Types

CLI tools, libraries, SDKs, APIs, web applications, monorepos, Chrome extensions, VS Code extensions, AI agents, MCP servers, RAG applications

## Safe Mode

This skill operates in safe mode by default:

- Never overwrites existing files unless explicitly requested
- Never generates placeholder content
- Never assumes technology without detection
- Always improves existing documentation when possible
- Always produces repository-specific output

## Agent Independence

Works with any AI coding agent that follows Markdown instructions:

- Claude Code / Opencode
- Cursor / Codex CLI
- Gemini CLI / Cline
- Aider / Continue

## Architecture

```
oss-ready/
├── skill.md              # Entry point and usage guide
├── AGENT.md              # Agent orchestration and command routing
├── prompt.md             # System prompt for the skill
├── reference.md          # Detection, scoring, output format (single source of truth)
├── checklist.md          # Readiness scoring tables
├── validation.md         # Skill quality and maintenance checklists
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
└── examples/             # Technology-specific guides
    ├── python.md
    ├── fastapi.md
    ├── react.md
    ├── nextjs.md
    ├── go.md
    ├── rust.md
    ├── cli.md
    ├── library.md
    └── chrome-extension.md
```

## Design Principles

1. **Single source of truth** — `reference.md` contains all detection tables, scoring methodology, and output formats. All other files reference it.
2. **Technology agnostic** — No assumptions about package managers, CI platforms, or languages. Everything is detected.
3. **Repository-specific** — Every generated artifact reflects the actual codebase, not generic templates.
4. **Safe by default** — Never overwrites existing files. Always explains what was generated and why.
5. **Modular** — Each agent has clear input/output contracts. No duplicated logic.

## Related Skills

- `opensource-pipeline` — Fork, sanitize, and package private projects for public release
- `security-review` — Security checklist for new projects
- `coding-standards` — Baseline coding conventions
- `repo-scan` — Repository audit and asset classification

## License

MIT
