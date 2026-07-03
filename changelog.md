# Changelog

All notable changes to the oss-ready skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [2.0.0] - 2026-07-03

### Added

- `reference.md` — single source of truth for detection, scoring, output format, and core rules
- `validation.md` — validation checklists for skill maintenance
- `changelog.md` — this file
- Go example (`examples/go.md`)
- Rust example (`examples/rust.md`)
- Expanded language detection: 20+ languages including Dart, Elixir, Scala, Haskell, Zig, Lua, R
- Expanded framework detection: 35+ frameworks including SolidJS, Nuxt, Astro, Remix, Fastify, Koa, Sanic, Quarkus, Actix Web, Axum, Rocket
- Expanded package manager detection: 16 managers including uv, pub, swift package manager
- Expanded build system detection: 15 systems including tsup, hatch, flit, pdm, just, task
- Expanded testing framework detection: 10+ frameworks
- Technology adaptation tables with correct commands for each language
- Repository type detection: CLI, SDK, library, monorepo, Chrome extension, VS Code extension, AI agent, MCP server, RAG application

### Changed

- `skill.md` — rewritten as concise entry point, references reference.md
- `AGENT.md` — rewritten to eliminate duplication, clear orchestration flow
- `prompt.md` — rewritten as clean system prompt, references reference.md
- `agents/audit.md` — rewritten to reference reference.md for detection and scoring
- `agents/docs.md` — rewritten with clear input/output contracts
- `agents/github.md` — rewritten with clear input/output contracts
- `agents/issues.md` — rewritten with clear input/output contracts
- `agents/architecture.md` — rewritten with clear input/output contracts
- `agents/roadmap.md` — rewritten with clear input/output contracts
- `agents/ci.md` — rewritten to be technology-agnostic, uses adaptation tables
- `agents/devex.md` — rewritten with clear input/output contracts
- `agents/release.md` — rewritten to be technology-agnostic
- `agents/report.md` — rewritten to reference reference.md for output format
- `checklist.md` — simplified to scoring tables only
- All templates — standardized format, removed technology bias, removed AI artifacts

### Removed

- Duplicated scoring methodology from agents/audit.md, agents/report.md, checklist.md
- Duplicated detection tables from agents/audit.md, skill.md, prompt.md
- Duplicated output format from AGENT.md, prompt.md, agents/audit.md
- Duplicated core rules from every agent file
- Duplicated technology adaptation from agents/docs.md, agents/ci.md, prompt.md
- Node.js-specific assumptions from CI/CD templates
- npm-specific assumptions from release templates
- Auto-generated footers from templates
- "Template Usage" sections from templates
- Emoji from template content
- AI-generated filler text from examples

## [1.0.0] - 2026-01-01

### Added

- Initial release of oss-ready skill
- Repository analysis and readiness scoring
- Documentation generation (README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, CHANGELOG)
- GitHub community files (issue templates, PR template, CODEOWNERS, labels)
- CI/CD workflow generation
- Developer experience documentation
- Release management documentation
- Architecture documentation
- Contribution opportunity identification
- Roadmap generation
- Readiness reporting
- Examples for Python, FastAPI, React, Next.js, CLI, Library, Chrome Extension
