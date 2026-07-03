# Reference: Single Source of Truth

This file contains the authoritative definitions for repository detection, scoring, output format, and core rules. All other files reference this document rather than duplicating content.

---

## Repository Detection

### Languages

| File Extension | Language |
|----------------|----------|
| `.py` | Python |
| `.js`, `.mjs`, `.cjs` | JavaScript |
| `.ts`, `.tsx`, `.jsx` | TypeScript |
| `.go` | Go |
| `.rs` | Rust |
| `.java` | Java |
| `.cs` | C# |
| `.cpp`, `.cc`, `.cxx`, `.h`, `.hpp` | C++ |
| `.php` | PHP |
| `.rb` | Ruby |
| `.swift` | Swift |
| `.kt`, `.kts` | Kotlin |
| `.lua` | Lua |
| `.r`, `.R` | R |
| `.ex`, `.exs` | Elixir |
| `.erl` | Erlang |
| `.hs` | Haskell |
| `.scala` | Scala |
| `.dart` | Dart |
| `.zig` | Zig |

Detect primary language by file count and lines of code.

### Frameworks

| Config File / Dependency | Framework |
|--------------------------|-----------|
| `react` in `package.json` | React |
| `next` in `package.json` | Next.js |
| `vue` in `package.json` | Vue |
| `@angular/core` in `package.json` | Angular |
| `svelte` in `package.json` | Svelte |
| `solid-js` in `package.json` | SolidJS |
| `nuxt` in `package.json` | Nuxt |
| `astro` in `package.json` | Astro |
| `remix` in `package.json` | Remix |
| `express` in `package.json` | Express |
| `@nestjs/core` in `package.json` | NestJS |
| `koa` in `package.json` | Koa |
| `fastify` in `package.json` | Fastify |
| `electron` in `package.json` | Electron |
| `react-native` in `package.json` | React Native |
| `flutter` / `pubspec.yaml` | Flutter |
| `fastapi` in `pyproject.toml` / `requirements.txt` | FastAPI |
| `django` in `pyproject.toml` / `requirements.txt` | Django |
| `flask` in `pyproject.toml` / `requirements.txt` | Flask |
| `sanic` in `pyproject.toml` / `requirements.txt` | Sanic |
| `tornado` in `pyproject.toml` / `requirements.txt` | Tornado |
| `spring-boot` in `pom.xml` / `build.gradle` | Spring Boot |
| `quarkus` in `pom.xml` / `build.gradle` | Quarkus |
| `laravel` in `composer.json` | Laravel |
| `rails` / `Gemfile` | Rails |
| `sinatra` in `Gemfile` | Sinatra |
| `gin` in `go.mod` | Gin |
| `echo` in `go.mod` | Echo |
| `fiber` in `go.mod` | Fiber |
| `actix-web` in `Cargo.toml` | Actix Web |
| `axum` in `Cargo.toml` | Axum |
| `rocket` in `Cargo.toml` | Rocket |

### Package Managers

| Lock / Config File | Package Manager |
|--------------------|-----------------|
| `package-lock.json` | npm |
| `yarn.lock` | yarn |
| `pnpm-lock.yaml` | pnpm |
| `bun.lockb` | bun |
| `requirements.txt` | pip |
| `Pipfile.lock` / `Pipfile` | pipenv |
| `poetry.lock` / `pyproject.toml` (poetry) | poetry |
| `uv.lock` | uv |
| `go.sum` | go mod |
| `Cargo.lock` / `Cargo.toml` | cargo |
| `pom.xml` | maven |
| `build.gradle` / `build.gradle.kts` | gradle |
| `composer.lock` / `composer.json` | composer |
| `Gemfile.lock` / `Gemfile` | bundler |
| `pubspec.lock` / `pubspec.yaml` | pub |
| `Package.resolved` / `Package.swift` | swift package manager |

### Build Systems

| Config File | Build System |
|-------------|--------------|
| `Makefile` | make |
| `CMakeLists.txt` | cmake |
| `webpack.config.*` | webpack |
| `vite.config.*` | vite |
| `rollup.config.*` | rollup |
| `esbuild.config.*` | esbuild |
| `tsconfig.json` | TypeScript (tsc) |
| `tsup.config.*` | tsup |
| `Cargo.toml` | cargo |
| `go.mod` | go build |
| `pom.xml` | maven |
| `build.gradle` | gradle |
| `pyproject.toml` | hatch / flit / pdm |
| `setup.py` / `setup.cfg` | setuptools |
| `Rakefile` | rake |
| `Justfile` | just |
| `Taskfile.yml` | task |

### Testing Frameworks

| Config / Dependency | Framework |
|---------------------|-----------|
| `jest.config.*` | Jest |
| `vitest.config.*` | Vitest |
| `.mocharc.*` | Mocha |
| `pytest.ini` / `conftest.py` / `pyproject.toml [tool.pytest]` | pytest |
| `unittest` in imports | unittest |
| `go test` | go test |
| `cargo test` | cargo test |
| `phpunit.xml` | PHPUnit |
| `junit` in `pom.xml` / `build.gradle` | JUnit |
| `rspec` in `Gemfile` | RSpec |
| `xctest` / `Package.swift` | XCTest |

### CI/CD Platforms

| Config File | Platform |
|-------------|----------|
| `.github/workflows/*.yml` | GitHub Actions |
| `.gitlab-ci.yml` | GitLab CI |
| `.circleci/config.yml` | CircleCI |
| `.travis.yml` | Travis CI |
| `Jenkinsfile` | Jenkins |
| `azure-pipelines.yml` | Azure Pipelines |
| `bitbucket-pipelines.yml` | Bitbucket Pipelines |
| `.drone.yml` | Drone CI |
| `cloudbuild.yaml` | Google Cloud Build |

### Project Types

| Indicators | Type |
|------------|------|
| `src/` with `index.*` or `main.*`, exports API | Library |
| `src/` with CLI entrypoint, `bin/` directory | CLI tool |
| `src/` with `server.*`, HTTP framework | API / Web service |
| `src/` with UI framework, `public/` | Application |
| Multiple `package.json` or `go.work` or workspace config | Monorepo |
| `manifest.json` with `content_scripts` | Chrome extension |
| `.vscodeignore`, `vsc-extension-quickstart.md` | VS Code extension |
| `mcp.json` or MCP protocol references | MCP server |
| Embedding/search dependencies | RAG application |
| Agent framework dependencies (agno, langchain, etc.) | AI agent |

---

## Scoring Methodology

### Dimensions and Weights

| Dimension | Weight |
|-----------|--------|
| Documentation | 25% |
| GitHub Community | 20% |
| CI/CD | 15% |
| Testing | 15% |
| Developer Experience | 15% |
| Security | 10% |

### Overall Score

```
Overall = (Documentation × 0.25) +
          (GitHub Community × 0.20) +
          (CI/CD × 0.15) +
          (Testing × 0.15) +
          (Developer Experience × 0.15) +
          (Security × 0.10)
```

### Documentation Score (0-100)

| Item | Points |
|------|--------|
| README.md exists and is comprehensive | 40 |
| CONTRIBUTING.md exists | 15 |
| CODE_OF_CONDUCT.md exists | 10 |
| SECURITY.md exists | 10 |
| SUPPORT.md exists | 10 |
| CHANGELOG.md exists | 10 |
| LICENSE exists | 5 |

### GitHub Community Score (0-100)

| Item | Points |
|------|--------|
| Issue templates exist | 30 |
| PR template exists | 20 |
| CODEOWNERS exists | 15 |
| Labels configured | 15 |
| Discussions enabled | 10 |
| FUNDING.yml exists | 10 |

### CI/CD Score (0-100)

| Item | Points |
|------|--------|
| Build workflow exists | 25 |
| Test workflow exists | 25 |
| Lint workflow exists | 25 |
| Release workflow exists | 25 |

### Testing Score (0-100)

| Item | Points |
|------|--------|
| Test framework configured | 30 |
| Test files exist | 30 |
| CI runs tests | 25 |
| Coverage configured | 15 |

### Developer Experience Score (0-100)

| Item | Points |
|------|--------|
| Setup instructions in README | 30 |
| Development guide exists | 25 |
| Coding standards documented | 20 |
| Commit conventions documented | 15 |
| Debugging guide exists | 10 |

### Security Score (0-100)

| Item | Points |
|------|--------|
| SECURITY.md exists | 30 |
| Dependency scanning configured | 25 |
| Secret scanning configured | 25 |
| No hardcoded secrets detected | 20 |

### Score Interpretation

| Score | Status | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Ready for open source |
| 70-89 | Good | Minor improvements needed |
| 50-69 | Fair | Significant improvements needed |
| 0-49 | Poor | Major work required |

---

## Output Format

All readiness reports must use this format:

```markdown
# Open Source Readiness Report

**Repository**: {name}
**Analyzed**: {timestamp}
**Overall Score**: {score}/100

---

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

| Dimension | Score | Weight | Weighted | Status |
|-----------|-------|--------|----------|--------|
| Documentation | X/100 | 25% | X | status |
| GitHub Community | X/100 | 20% | X | status |
| CI/CD | X/100 | 15% | X | status |
| Testing | X/100 | 15% | X | status |
| Developer Experience | X/100 | 15% | X | status |
| Security | X/100 | 10% | X | status |
| **Overall** | | | **X/100** | |

## Generated Artifacts

- status artifact (description)

## Recommendations

### High Priority
1. {recommendation}

### Medium Priority
1. {recommendation}

### Low Priority
1. {recommendation}

## Next Steps

1. {action}
```

---

## Core Rules

These rules apply to every agent and every output.

### Safe Mode

- Never overwrite existing files unless explicitly requested
- Never generate placeholder content
- Never make assumptions without repository analysis
- Always improve existing documentation when possible
- Always produce repository-specific content
- Always explain what was generated and why

### Quality Gates

Before writing any file, verify:

- Content is repository-specific (not generic)
- All code examples use actual project code
- All file paths reference real files
- All instructions are accurate for this technology stack
- No placeholder text remains
- No hallucinated features or capabilities

### Anti-Patterns

- Never generate without analyzing the repository first
- Never use generic templates without customization
- Never overwrite existing files without user permission
- Never invent features or capabilities the project doesn't have
- Never skip the audit phase
- Never ignore existing documentation (improve it instead)

---

## Technology Adaptation

When generating content, adapt to the detected stack:

### By Language

| Language | Config File | Install Command | Test Command | Lint Command | Format Command |
|----------|-------------|-----------------|--------------|--------------|----------------|
| Python | `pyproject.toml`, `setup.py` | `pip install -e ".[dev]"` | `pytest` | `ruff check .` | `ruff format .` |
| JavaScript | `package.json` | `npm ci` | `npm test` | `npm run lint` | `npm run format` |
| TypeScript | `package.json` | `npm ci` | `npm test` | `npm run lint` | `npm run format` |
| Go | `go.mod` | `go mod download` | `go test ./...` | `golangci-lint run` | `gofmt -w .` |
| Rust | `Cargo.toml` | `cargo fetch` | `cargo test` | `cargo clippy` | `cargo fmt` |
| Java | `pom.xml`, `build.gradle` | `mvn install` / `gradle build` | `mvn test` / `gradle test` | `checkstyle` | — |
| Kotlin | `build.gradle.kts` | `gradle build` | `gradle test` | `ktlint` | `ktlintFormat` |
| C# | `*.csproj` | `dotnet restore` | `dotnet test` | — | — |
| C++ | `CMakeLists.txt` | `cmake --build .` | `ctest` | `clang-tidy` | `clang-format` |
| PHP | `composer.json` | `composer install` | `vendor/bin/phpunit` | `phpstan` | `php-cs-fixer` |
| Ruby | `Gemfile` | `bundle install` | `bundle exec rspec` | `rubocop` | `rubocop -A` |
| Swift | `Package.swift` | `swift package resolve` | `swift test` | `swiftlint` | `swiftformat` |
| Dart | `pubspec.yaml` | `dart pub get` | `dart test` | `dart analyze` | `dart format` |
| Elixir | `mix.exs` | `mix deps.get` | `mix test` | `mix credo` | `mix format` |

### By Framework

When the detected framework has specific conventions, follow them:
- React/Next.js: Use JSX/TSX, reference component patterns
- FastAPI: Use async/await, Pydantic models, OpenAPI docs
- Django: Use ORM patterns, settings.py conventions
- Spring Boot: Use annotations, application.properties
- Laravel: Use Eloquent, artisan commands
- Rails: Use ActiveRecord, rake tasks
- Express/NestJS: Use middleware patterns, decorators
