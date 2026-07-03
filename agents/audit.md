# Audit Agent

Analyze a repository and generate an Open Source Readiness Report.

## Purpose

The Audit Agent inspects a repository to understand its structure, technology stack, and current state of open source readiness. It produces a comprehensive report that guides all subsequent artifact generation.

## When to Use

- Before generating any documentation
- When assessing repository health
- When planning open source release
- When onboarding to an existing project

## Analysis Protocol

### Phase 1: Project Structure

Analyze the repository root and identify:

```
□ Project type (application, library, CLI, API, monorepo)
□ Directory structure (src/, lib/, test/, docs/, etc.)
□ Configuration files (package.json, pyproject.toml, Cargo.toml, etc.)
□ Entry points (main files, index files, CLI entrypoints)
□ Build outputs (dist/, build/, bin/, etc.)
```

### Phase 2: Technology Detection

#### Languages

Analyze file extensions to detect languages:

| Extension | Language |
|-----------|----------|
| `.py` | Python |
| `.js`, `.mjs`, `.cjs` | JavaScript |
| `.ts`, `.tsx`, `.jsx` | TypeScript |
| `.go` | Go |
| `.rs` | Rust |
| `.java` | Java |
| `.cs` | C# |
| `.cpp`, `.cc`, `.h` | C++ |
| `.php` | PHP |
| `.rb` | Ruby |
| `.swift` | Swift |
| `.kt` | Kotlin |

Calculate primary language by file count and lines of code.

#### Frameworks

Detect frameworks from configuration files and dependencies:

| Config/Dependency | Framework |
|-------------------|-----------|
| `react` in package.json | React |
| `next` in package.json | Next.js |
| `vue` in package.json | Vue |
| `@angular/core` in package.json | Angular |
| `fastapi` in pyproject.toml/requirements.txt | FastAPI |
| `django` in pyproject.toml/requirements.txt | Django |
| `flask` in pyproject.toml/requirements.txt | Flask |
| `spring-boot` in pom.xml/build.gradle | Spring Boot |
| `@nestjs/core` in package.json | NestJS |
| `express` in package.json | Express |

#### Package Managers

Detect from lockfiles and config files:

| File | Package Manager |
|------|-----------------|
| `package-lock.json` | npm |
| `yarn.lock` | yarn |
| `pnpm-lock.yaml` | pnpm |
| `bun.lockb` | bun |
| `requirements.txt` | pip |
| `Pipfile.lock` | pipenv |
| `poetry.lock` | poetry |
| `uv.lock` | uv |
| `go.sum` | go mod |
| `Cargo.lock` | cargo |
| `pom.xml` | maven |
| `build.gradle` | gradle |
| `composer.lock` | composer |

#### Build Systems

Detect from configuration files:

| File | Build System |
|------|--------------|
| `Makefile` | make |
| `CMakeLists.txt` | cmake |
| `webpack.config.*` | webpack |
| `vite.config.*` | vite |
| `rollup.config.*` | rollup |
| `esbuild.config.*` | esbuild |
| `tsconfig.json` | TypeScript |
| `Cargo.toml` | cargo |
| `go.mod` | go build |

### Phase 3: Testing Assessment

Analyze testing setup:

```
□ Test framework detected (pytest, jest, vitest, go test, cargo test, etc.)
□ Test files located (test/, tests/, __tests__/, *_test.go, *_test.py, etc.)
□ Test configuration found (jest.config.*, pytest.ini, etc.)
□ CI integration checked (workflows running tests)
□ Coverage configuration found (coverage config, thresholds)
```

### Phase 4: CI/CD Assessment

Check for existing workflows:

```
□ GitHub Actions (.github/workflows/*.yml)
□ GitLab CI (.gitlab-ci.yml)
□ CircleCI (.circleci/config.yml)
□ Travis CI (.travis.yml)
□ Jenkins (Jenkinsfile)
□ Other CI configurations
```

For each workflow found, identify:
- What it does (build, test, lint, release)
- What triggers it (push, PR, schedule)
- What it produces (artifacts, deployments)

### Phase 5: Documentation Assessment

Check for existing documentation:

```
□ README.md — Does it exist? Quality assessment?
□ CONTRIBUTING.md — Does it exist?
□ CODE_OF_CONDUCT.md — Does it exist?
□ SECURITY.md — Does it exist?
□ SUPPORT.md — Does it exist?
□ CHANGELOG.md — Does it exist?
□ LICENSE — Does it exist? Which license?
□ docs/ directory — Does it exist?
□ API documentation — Does it exist?
□ Code comments — Adequate documentation?
```

### Phase 6: GitHub Community Assessment

Check for GitHub community files:

```
□ Issue templates (.github/ISSUE_TEMPLATE/)
□ Pull request template (.github/PULL_REQUEST_TEMPLATE.md)
□ CODEOWNERS (.github/CODEOWNERS)
□ FUNDING.yml (.github/FUNDING.yml)
□ Discussions enabled
□ Wiki enabled
□ Labels configured
```

### Phase 7: Repository Maturity

Assess maturity indicators:

```
□ Commit history (how many commits?)
□ Contributors (how many contributors?)
□ Release tags (any semantic version tags?)
□ Dependency freshness (are dependencies up to date?)
□ Security advisories (any known vulnerabilities?)
□ Community activity (issues, PRs, discussions?)
```

## Output Format

Generate a readiness report in this format:

```markdown
# Open Source Readiness Report

**Repository**: {name}
**Analyzed**: {timestamp}
**Overall Score**: {score}/100

## Project Overview

| Property | Value |
|----------|-------|
| Type | {application/library/cli/api/monorepo} |
| Primary Language | {language} ({percentage}%) |
| Framework | {framework or "None detected"} |
| Package Manager | {manager} |
| Build System | {system} |
| License | {license or "Not found"} |

## Readiness Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Documentation | X/100 | 25% | X |
| GitHub Community | X/100 | 20% | X |
| CI/CD | X/100 | 15% | X |
| Testing | X/100 | 15% | X |
| Developer Experience | X/100 | 15% | X |
| Security | X/100 | 10% | X |
| **Overall** | | | **X/100** |

## Documentation Status

| File | Exists | Quality | Action |
|------|--------|---------|--------|
| README.md | ✅/❌ | Good/Fair/Poor | Keep/Create/Improve |
| CONTRIBUTING.md | ✅/❌ | - | Create |
| CODE_OF_CONDUCT.md | ✅/❌ | - | Create |
| SECURITY.md | ✅/❌ | - | Create |
| SUPPORT.md | ✅/❌ | - | Create |
| CHANGELOG.md | ✅/❌ | - | Create |
| LICENSE | ✅/❌ | - | Create |

## GitHub Community Status

| File | Exists | Action |
|------|--------|--------|
| Issue templates | ✅/❌ | Create |
| PR template | ✅/❌ | Create |
| CODEOWNERS | ✅/❌ | Create |
| FUNDING.yml | ✅/❌ | Skip |

## CI/CD Status

| Workflow | Exists | Purpose |
|----------|--------|---------|
| Build | ✅/❌ | {purpose} |
| Test | ✅/❌ | {purpose} |
| Lint | ✅/❌ | {purpose} |
| Release | ✅/❌ | {purpose} |

## Testing Status

| Metric | Value |
|--------|-------|
| Framework | {framework} |
| Test files | {count} |
| Coverage config | ✅/❌ |
| CI integration | ✅/❌ |

## Recommendations

### High Priority
1. {recommendation}
2. {recommendation}

### Medium Priority
1. {recommendation}
2. {recommendation}

### Low Priority
1. {recommendation}

## Generated Artifacts

List all artifacts that will be generated based on this audit.
```

## Scoring Methodology

### Documentation Score (0-100)

- README.md exists and is comprehensive: 40 points
- CONTRIBUTING.md exists: 15 points
- CODE_OF_CONDUCT.md exists: 10 points
- SECURITY.md exists: 10 points
- SUPPORT.md exists: 10 points
- CHANGELOG.md exists: 10 points
- LICENSE exists: 5 points

### GitHub Community Score (0-100)

- Issue templates exist: 30 points
- PR template exists: 20 points
- CODEOWNERS exists: 15 points
- Labels configured: 15 points
- Discussions enabled: 10 points
- FUNDING.yml exists: 10 points

### CI/CD Score (0-100)

- Build workflow exists: 25 points
- Test workflow exists: 25 points
- Lint workflow exists: 25 points
- Release workflow exists: 25 points

### Testing Score (0-100)

- Test framework configured: 30 points
- Test files exist: 30 points
- CI runs tests: 25 points
- Coverage configured: 15 points

### Developer Experience Score (0-100)

- Setup instructions in README: 30 points
- Development guide exists: 25 points
- Coding standards documented: 20 points
- Commit conventions documented: 15 points
- Debugging guide exists: 10 points

### Security Score (0-100)

- SECURITY.md exists: 30 points
- Dependency scanning configured: 25 points
- Secret scanning configured: 25 points
- No hardcoded secrets detected: 20 points

## Instructions

1. Execute all analysis phases systematically
2. Be thorough — check every item in the checklists
3. Be honest — report actual state, not ideal state
4. Be specific — reference actual files and configurations
5. Generate the report in the specified format
6. Prioritize recommendations by impact and effort
