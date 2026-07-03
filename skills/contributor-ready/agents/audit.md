# Audit Agent

Analyze a repository and produce an Open Source Readiness Report.

## Purpose

Inspect a repository to understand its structure, technology stack, and current state of open source readiness. The audit output guides all subsequent artifact generation.

## Input

- Repository path
- `reference.md` for detection tables and scoring methodology

## Output

A readiness report following the format defined in `reference.md`.

## Analysis Protocol

### Phase 1: Project Structure

Read the repository root and identify:
- Project type (application, library, CLI, API, monorepo — see `reference.md` for indicators)
- Directory structure (`src/`, `lib/`, `test/`, `docs/`, etc.)
- Configuration files (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.)
- Entry points (main files, index files, CLI entrypoints)
- Build outputs (`dist/`, `build/`, `bin/`, etc.)

### Phase 2: Technology Detection

Use the detection tables in `reference.md` to identify:

1. **Languages** — Primary and secondary by file count and lines of code
2. **Frameworks** — From config files and dependencies
3. **Package managers** — From lockfiles and config files
4. **Build systems** — From configuration files
5. **Testing frameworks** — From config and test file patterns
6. **CI/CD platforms** — From workflow configuration files

### Phase 3: Documentation Assessment

Check for existing documentation:
- README.md — exists? quality assessment?
- CONTRIBUTING.md — exists?
- CODE_OF_CONDUCT.md — exists?
- SECURITY.md — exists?
- SUPPORT.md — exists?
- CHANGELOG.md — exists?
- LICENSE — exists? which license?
- `docs/` directory — exists?
- API documentation — exists?
- Code comments — adequate?

### Phase 4: GitHub Community Assessment

Check for GitHub community files:
- Issue templates (`.github/ISSUE_TEMPLATE/`)
- Pull request template (`.github/PULL_REQUEST_TEMPLATE.md`)
- CODEOWNERS (`.github/CODEOWNERS`)
- FUNDING.yml (`.github/FUNDING.yml`)
- Discussions enabled
- Labels configured

### Phase 5: CI/CD Assessment

Check for existing workflows. For each workflow found, identify:
- What it does (build, test, lint, release)
- What triggers it (push, PR, schedule)
- What it produces (artifacts, deployments)

### Phase 6: Testing Assessment

Analyze testing setup:
- Test framework detected
- Test files located
- Test configuration found
- CI integration checked
- Coverage configuration found

### Phase 7: Repository Maturity

Assess maturity indicators:
- Commit history (count, frequency)
- Contributors (count, activity)
- Release tags (semantic version tags?)
- Dependency freshness
- Community activity (issues, PRs, discussions)

## Scoring

Use the scoring methodology from `reference.md`. Do not invent alternative scoring systems. The six dimensions and their weights are defined there.

## Instructions

1. Execute all analysis phases systematically
2. Be thorough — check every item in the checklists
3. Be honest — report actual state, not ideal state
4. Be specific — reference actual files and configurations
5. Generate the report using the output format from `reference.md`
6. Prioritize recommendations by impact and effort
