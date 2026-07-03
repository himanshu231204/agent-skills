# agent-skills

[![skills.sh](https://skills.sh/b/himanshu231204/agent-skills)](https://skills.sh/himanshu231204/agent-skills)

A curated collection of production-quality AI coding agent skills for repository analysis, documentation, code quality, architecture, developer experience, and open source maintenance.

## What Are AI Coding Agent Skills?

AI coding agent skills are reusable instruction sets that teach AI coding agents how to perform specialized tasks. Each skill is a self-contained directory with Markdown instructions, templates, and reference data that an agent loads dynamically to improve its performance on a specific workflow.

Skills work with any AI coding agent that follows Markdown instructions — Claude Code, OpenCode, Cursor, Codex CLI, Gemini CLI, Cline, Aider, and more.

## Repository Structure

```
agent-skills/
├── README.md
├── LICENSE
├── .gitignore
├── skills/
│   └── contributor-ready/
│       ├── skill.md              # Entry point
│       ├── AGENT.md              # Agent orchestration
│       ├── prompt.md             # System prompt
│       ├── reference.md          # Single source of truth
│       ├── checklist.md          # Scoring tables
│       ├── validation.md         # Quality checklists
│       ├── changelog.md          # Version history
│       ├── quality-report.md     # Quality assessment
│       ├── agents/               # Specialized agent instructions
│       ├── templates/            # Documentation templates
│       ├── examples/             # Technology-specific guides
│       └── assets/               # Static resources
└── docs/                         # Documentation
```

## Available Skills

| Skill | Description | Status |
|-------|-------------|--------|
| [contributor-ready](skills/contributor-ready/) | Transform any repository into a contributor-friendly, production-ready open source project | Available |

## Installation

### Install a Skill

```bash
# Install contributor-ready
npx skills add https://github.com/himanshu231204/agent-skills --skill contributor-ready
```

### Browse and Install

```bash
# List available skills
npx skills list https://github.com/himanshu231204/agent-skills

# Install a specific skill
npx skills add https://github.com/himanshu231204/agent-skills --skill <skill-name>
```

## How to Use

After installing a skill, invoke it in your AI coding agent:

```
Run contributor-ready full on this repository to make it contributor-ready.
```

Each skill defines its own commands and workflow. See the individual skill's README for specific usage instructions.

## How to Contribute

We welcome contributions of new skills and improvements to existing ones.

### Adding a New Skill

1. Create a new directory under `skills/` with your skill name
2. Add a `skill.md` file with YAML frontmatter (name, description)
3. Add `AGENT.md` for orchestration instructions
4. Add `reference.md` for any skill-specific reference data
5. Add a `README.md` with installation and usage instructions
6. Submit a pull request

### Skill Directory Structure

```
skills/your-skill-name/
├── skill.md           # Required: entry point with frontmatter
├── AGENT.md           # Required: orchestration and command routing
├── prompt.md          # Optional: system prompt
├── reference.md       # Optional: reference data
├── agents/            # Optional: specialized agent instructions
├── templates/         # Optional: reusable templates
├── examples/          # Optional: usage examples
└── README.md          # Required: documentation
```

### Quality Standards

All skills should:

- Be agent-independent (work with any AI coding agent)
- Be technology-agnostic (no hardcoded assumptions)
- Include clear documentation
- Follow the single-source-of-truth pattern
- Include a validation checklist

## Roadmap

### Planned Skills

| Skill | Description | Status |
|-------|-------------|--------|
| code-review-pro | Automated code review with security, performance, and style analysis | Planned |
| architecture-review | System architecture analysis and improvement recommendations | Planned |
| docs-generator | Comprehensive documentation generation from source code | Planned |
| api-docs | API documentation generation with OpenAPI/Swagger support | Planned |
| release-manager | Release automation, versioning, and changelog management | Planned |
| security-audit | Security vulnerability scanning and remediation guidance | Planned |
| ai-project-review | AI/ML project structure, model management, and MLOps review | Planned |
| performance-review | Performance profiling, optimization, and monitoring setup | Planned |

### Contributing a Skill

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines on creating and submitting new skills.

## License

MIT
