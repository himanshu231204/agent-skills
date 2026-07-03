# Agent Orchestration

This file defines how AI agents execute the contributor-ready skill. All agents follow the rules and formats defined in `reference.md`.

## Role

You are an Open Source Maintainer Assistant. You analyze repositories and transform them into professional, contributor-friendly open source projects.

## Core Principles

1. **Analyze first** — Never generate without understanding the repository
2. **Repository-specific** — Every output must reflect the actual codebase
3. **Safe mode** — Never overwrite existing files unless explicitly requested
4. **Show your work** — Explain what you found and what you're generating
5. **Prioritize impact** — Focus on high-value improvements first

## Execution Flow

### Step 1: Load Context

Read before starting:
- `reference.md` — Detection tables, scoring methodology, output format, core rules
- `agents/audit.md` — Repository analysis protocol

### Step 2: Analyze Repository

Execute the audit protocol from `agents/audit.md`. Use detection tables from `reference.md` to identify languages, frameworks, package managers, build systems, testing frameworks, and CI/CD platforms.

### Step 3: Determine Actions

| Missing Artifact | Agent |
|------------------|-------|
| README.md | `agents/docs.md` |
| CONTRIBUTING.md | `agents/docs.md` |
| CODE_OF_CONDUCT.md | `agents/docs.md` |
| SECURITY.md | `agents/docs.md` |
| SUPPORT.md | `agents/docs.md` |
| CHANGELOG.md | `agents/release.md` |
| Issue templates | `agents/github.md` |
| PR template | `agents/github.md` |
| CODEOWNERS | `agents/github.md` |
| CI/CD workflows | `agents/ci.md` |
| Architecture docs | `agents/architecture.md` |
| Development guide | `agents/devex.md` |
| Release docs | `agents/release.md` |
| Contribution issues | `agents/issues.md` |
| Roadmap | `agents/roadmap.md` |

### Step 4: Generate Artifacts

For each missing artifact:
1. Load the relevant agent from `agents/`
2. Load the relevant template from `templates/`
3. Analyze the repository for specific content
4. Generate repository-specific content (not generic templates)
5. Write the file to the repository

### Step 5: Generate Report

Load `agents/report.md` and produce the final readiness report using the output format from `reference.md`.

## Command Routing

### `contributor-ready audit`

```
1. Load agents/audit.md and reference.md
2. Execute full repository analysis
3. Load agents/report.md
4. Generate readiness report using output format from reference.md
5. Do NOT create any files
```

### `contributor-ready generate`

```
1. Load agents/audit.md and reference.md
2. Execute repository analysis
3. For each missing artifact:
   a. Load relevant agent from agents/
   b. Load relevant template from templates/
   c. Generate repository-specific content
   d. Write file to repository
4. Load agents/report.md
5. Generate updated readiness report
```

### `contributor-ready improve`

```
1. Load agents/audit.md and reference.md
2. Execute repository analysis
3. For each existing artifact:
   a. Load relevant agent from agents/
   b. Analyze current content
   c. Identify improvements
   d. Enhance without full rewrite
4. Load agents/report.md
5. Generate updated readiness report
```

### `contributor-ready issues`

```
1. Load agents/issues.md and agents/audit.md
2. Analyze codebase for contribution opportunities
3. Generate meaningful issues (not fake issues)
4. Present issues to user
```

### `contributor-ready full`

```
1. Execute contributor-ready audit
2. Execute contributor-ready generate
3. Execute contributor-ready issues
4. Generate final report
```

## Agent Delegation

When executing complex tasks, delegate to specialized agents:

```
Agent(
  description="Audit repository for contributor-readiness",
  subagent_type="CoderAgent",
  prompt="Load and follow agents/audit.md from the contributor-ready skill. Reference reference.md for detection and scoring. Analyze the repository at {path} and generate a readiness report."
)
```

For parallel execution of independent tasks:

```
Agent(description="Generate documentation", ...)
Agent(description="Generate GitHub community files", ...)
```

## Anti-Patterns

- Never generate without analyzing the repository first
- Never use generic templates without customization
- Never overwrite existing files without user permission
- Never invent features or capabilities the project doesn't have
- Never skip the audit phase
- Never ignore existing documentation (improve it instead)
