# CI/CD Agent

Generate and improve CI/CD workflows.

## Purpose

Inspect existing workflows and generate missing ones. Create build, test, lint, and release pipelines that follow best practices for the detected technology stack.

## Input

- Repository analysis from `agents/audit.md`
- Detected CI/CD platform (from `reference.md`)
- Detected language, framework, package manager (from `reference.md`)

## Output

CI/CD workflow files written to the appropriate CI directory (e.g., `.github/workflows/`, `.gitlab-ci.yml`).

## Platform Detection

Use `reference.md` to detect the CI/CD platform. Default to GitHub Actions if no platform is detected and the user wants CI/CD.

## Workflows to Generate

### Build Workflow
- Triggered on push to main/develop and PRs
- Installs dependencies using detected package manager
- Builds the project using detected build system
- Uploads build artifacts

### Test Workflow
- Triggered on push to main/develop and PRs
- Runs test suite using detected testing framework
- Uploads coverage reports (if configured)

### Lint Workflow
- Triggered on push to main/develop and PRs
- Runs linter using detected linting tool
- Checks formatting using detected formatter

### Release Workflow
- Triggered on version tags (e.g., `v*`)
- Builds, tests, creates GitHub release
- Publishes to package manager (if applicable)

### Security Scanning Workflow
- Scheduled and on PRs
- Runs dependency vulnerability scanning
- Runs static analysis (CodeQL or equivalent)

## Technology Adaptation

Use the adaptation tables in `reference.md` to generate correct commands for the detected stack. Key variables:
- Setup command (setup-node, setup-python, setup-go, etc.)
- Install command (npm ci, pip install, go mod download, etc.)
- Build command (npm run build, go build, cargo build, etc.)
- Test command (npm test, pytest, go test, cargo test, etc.)
- Lint command (npm run lint, ruff check, golangci-lint, etc.)
- Format command (npm run format, ruff format, gofmt, etc.)

## Generation Rules

### Always Do
- Use the latest action versions
- Cache dependencies
- Run on multiple versions when applicable
- Include proper error handling
- Use secrets for sensitive data
- Adapt to the detected technology stack

### Never Do
- Hardcode secrets
- Skip tests before release
- Use outdated actions
- Ignore security scanning
- Skip the analysis phase
- Generate Node.js-only workflows for non-JS projects
