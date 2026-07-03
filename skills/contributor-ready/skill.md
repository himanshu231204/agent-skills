---
name: contributor-ready
description: "Transform any software repository into a contributor-friendly, production-ready open source project. Analyzes repo health, generates documentation, creates GitHub community files, identifies contribution opportunities, and produces a readiness report. Agent-independent and technology-agnostic."
---

# contributor-ready

> The universal AI coding agent skill for preparing repositories for open source contributors.

Analyze, document, and prepare any repository for open source contribution. This skill does not generate generic templates — it inspects your actual codebase and produces repository-specific artifacts.

## Commands

| Command | What It Does |
|---------|--------------|
| `contributor-ready audit` | Analyze repository, produce readiness report (no file changes) |
| `contributor-ready generate` | Create only the files that are missing |
| `contributor-ready improve` | Enhance existing documentation in place |
| `contributor-ready issues` | Identify real contribution opportunities from code analysis |
| `contributor-ready full` | Audit, generate, issues, report — complete pipeline |

## Quick Start

```
Run contributor-ready full on this repository to make it contributor-ready.
```

## How It Works

1. **Analyze** — Detect project type, languages, frameworks, tooling, and current open source readiness
2. **Score** — Rate six dimensions (Documentation, GitHub Community, CI/CD, Testing, Developer Experience, Security) using weighted scoring from `reference.md`
3. **Generate** — Create missing artifacts using templates and repository-specific content
4. **Report** — Produce a readiness report with scores, generated artifacts, and prioritized next steps

## Safe Mode

- Never overwrites existing files unless explicitly requested
- Never generates placeholder content
- Never assumes technology without detection
- Always improves existing documentation when possible
- Always produces repository-specific output

To regenerate an existing file, request it explicitly:

```
Regenerate the README.md for this repository.
```

## Architecture

```
contributor-ready/
├── skill.md              # Entry point — this file
├── AGENT.md              # Agent orchestration and command routing
├── prompt.md             # System prompt for the skill
├── reference.md          # Detection, scoring, output format (single source of truth)
├── checklist.md          # Readiness scoring tables
├── validation.md         # Skill quality and maintenance checklists
├── changelog.md          # Improvement history
├── quality-report.md     # Quality assessment report
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
│   ├── go.md
│   ├── rust.md
│   ├── cli.md
│   ├── library.md
│   └── chrome-extension.md
└── assets/               # Static assets and resources
```

## Technology Support

**Languages**: Python, JavaScript, TypeScript, Go, Rust, Java, C#, C++, PHP, Ruby, Swift, Kotlin, Dart, Elixir, Scala, Haskell, Zig, Lua, R

**Frameworks**: React, Next.js, Vue, Angular, Svelte, Nuxt, Astro, Remix, Express, NestJS, Fastify, Koa, FastAPI, Django, Flask, Sanic, Spring Boot, Quarkus, Laravel, Rails, Sinatra, Gin, Echo, Fiber, Actix Web, Axum, Rocket, Flutter, Electron, React Native

**Tools**: CLI applications, browser extensions, VS Code extensions, mobile apps, desktop apps, libraries, SDKs, monorepos, MCP servers, AI agents, RAG applications

## Related Skills

- `opensource-pipeline` — Fork, sanitize, and package private projects for public release
- `security-review` — Security checklist for new projects
- `coding-standards` — Baseline coding conventions
- `repo-scan` — Repository audit and asset classification

## License

MIT
