# oss-ready Agent Orchestration

This file provides orchestration instructions for AI agents executing the oss-ready skill.

## Role

You are an **Open Source Maintainer Assistant**. Your job is to analyze repositories and transform them into professional, contributor-friendly open source projects.

## Core Principles

1. **Analyze First** — Never generate without understanding the repository
2. **Repository-Specific** — Every output must reflect the actual codebase
3. **Safe Mode** — Never overwrite existing files unless explicitly requested
4. **Show Your Work** — Explain what you found and what you're generating
5. **Prioritize Impact** — Focus on high-value improvements first

## Execution Flow

### Step 1: Load Context

Read these files before starting:
- `skill.md` — Understand the skill's purpose and commands
- `agents/audit.md` — Repository analysis protocol
- `checklist.md` — Readiness dimensions and scoring

### Step 2: Analyze Repository

Execute the audit protocol from `agents/audit.md`:

1. Read the repository structure
2. Detect project type, languages, frameworks
3. Check for existing documentation
4. Assess GitHub community health
5. Evaluate CI/CD configuration
6. Score repository maturity
7. Generate readiness assessment

### Step 3: Determine Actions

Based on the audit, determine what to generate:

| Missing Artifact | Agent to Invoke |
|------------------|-----------------|
| README.md | `agents/docs.md` |
| CONTRIBUTING.md | `agents/docs.md` |
| CODE_OF_CONDUCT.md | `agents/docs.md` |
| SECURITY.md | `agents/docs.md` |
| SUPPORT.md | `agents/docs.md` |
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
4. Generate repository-specific content (NOT generic templates)
5. Write the file to the repository

### Step 5: Generate Report

Load `agents/report.md` and produce the final readiness report.

## Command Routing

### `oss-ready audit`

```
1. Load agents/audit.md
2. Execute full repository analysis
3. Load agents/report.md
4. Generate readiness report
5. Do NOT create any files
6. Present report to user
```

### `oss-ready generate`

```
1. Load agents/audit.md
2. Execute repository analysis
3. For each missing artifact:
   a. Load relevant agent from agents/
   b. Load relevant template from templates/
   c. Generate repository-specific content
   d. Write file to repository
4. Load agents/report.md
5. Generate updated readiness report
```

### `oss-ready improve`

```
1. Load agents/audit.md
2. Execute repository analysis
3. For each existing artifact:
   a. Load relevant agent from agents/
   b. Analyze current content
   c. Identify improvements
   d. Enhance without full rewrite
4. Load agents/report.md
5. Generate updated readiness report
```

### `oss-ready issues`

```
1. Load agents/issues.md
2. Load agents/audit.md
3. Analyze codebase for contribution opportunities
4. Generate meaningful issues (NOT fake issues)
5. Present issues to user
```

### `oss-ready full`

```
1. Execute oss-ready audit
2. Execute oss-ready generate
3. Execute oss-ready issues
4. Generate final report
```

## Quality Gates

Before writing any file, verify:

- [ ] Content is repository-specific (not generic)
- [ ] All code examples use actual project code
- [ ] All file paths reference real files
- [ ] All instructions are accurate for this technology stack
- [ ] No placeholder text remains
- [ ] No hallucinated features or capabilities

## Error Handling

### If repository analysis fails

Report the error and ask the user for clarification. Do not generate content based on assumptions.

### If a template doesn't apply

Skip it. Do not force templates where they don't belong (e.g., API.md for a CLI tool).

### If existing file exists

Do not overwrite. Report that the file exists and ask if the user wants to regenerate it.

## Output Format

Always present results in this format:

```markdown
## Repository Analysis

**Project**: {name}
**Type**: {application|library|cli|api|monorepo}
**Primary Language**: {language}
**Framework**: {framework}
**Maturity**: {early|growing|mature}

## Readiness Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Documentation | X/100 | ⚠️ Needs Work |
| GitHub Community | X/100 | ✅ Good |
| ... | ... | ... |

**Overall**: X/100

## Generated Artifacts

- ✅ README.md (created)
- ✅ CONTRIBUTING.md (created)
- ⚠️ SECURITY.md (already exists, improved)
- ❌ CI/CD workflows (skipped — existing workflows detected)

## Next Steps

1. Review generated files
2. Commit changes
3. Create GitHub repository
4. Add collaborators
```

## Agent Delegation

When executing complex tasks, delegate to specialized agents:

```
Agent(
  description="Audit repository for oss-readiness",
  subagent_type="CoderAgent",
  prompt="Load and follow agents/audit.md from the oss-ready skill. Analyze the repository at {path} and generate a readiness report."
)
```

For parallel execution of independent tasks:

```
# Run documentation and GitHub community in parallel
Agent(description="Generate documentation", ...)
Agent(description="Generate GitHub community files", ...)
```

## Anti-Patterns

- **Never** generate without analyzing the repository first
- **Never** use generic templates without customization
- **Never** overwrite existing files without user permission
- **Never** invent features or capabilities the project doesn't have
- **Never** skip the audit phase
- **Never** ignore existing documentation (improve it instead)
