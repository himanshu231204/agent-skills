# Open Source Readiness Checklist

Use this checklist to evaluate and improve your repository's open source readiness.

## Documentation

### Essential Files

- [ ] **README.md** — Clear project description, installation, usage, contributing
- [ ] **CONTRIBUTING.md** — Contribution guidelines, development setup, PR process
- [ ] **CODE_OF_CONDUCT.md** — Community standards, enforcement
- [ ] **SECURITY.md** — Security policy, vulnerability reporting
- [ ] **SUPPORT.md** — How to get help, FAQ
- [ ] **CHANGELOG.md** — Version history, release notes
- [ ] **LICENSE** — Open source license

### Documentation Quality

- [ ] **Clear description** — What the project does and why
- [ ] **Installation instructions** — Step-by-step setup
- [ ] **Usage examples** — Working code examples
- [ ] **API documentation** — Function/method documentation
- [ ] **Configuration guide** — Environment variables, config files
- [ ] **Troubleshooting** — Common issues and solutions
- [ ] **Screenshots/GIFs** — Visual demonstrations (if applicable)

### Code Documentation

- [ ] **Inline comments** — Explain complex logic
- [ ] **Function documentation** — JSDoc/TSDoc/docstrings
- [ ] **Type definitions** — TypeScript types, Python type hints
- [ ] **Code examples** — In-code examples and usage

## GitHub Community

### Issue Management

- [ ] **Bug report template** — Structured bug reporting
- [ ] **Feature request template** — Feature suggestion format
- [ ] **Documentation template** — Documentation improvement format
- [ ] **Good first issue template** — Contributor-friendly issues

### Pull Requests

- [ ] **PR template** — Structured PR description
- [ ] **Review process** — Clear review guidelines
- [ ] **Merge strategy** — Squash, merge, or rebase

### Community Health

- [ ] **CODEOWNERS** — Code ownership definition
- [ ] **Labels** — Organized issue/PR labels
- [ ] **Milestones** — Release planning
- [ ] **Projects** — Project boards (optional)
- [ ] **Discussions** — Community Q&A (optional)
- [ ] **FUNDING.yml** — Sponsorship information (optional)

## CI/CD

### Workflows

- [ ] **Build workflow** — Verify code compiles/builds
- [ ] **Test workflow** — Run test suite
- [ ] **Lint workflow** — Code style checking
- [ ] **Format workflow** — Code formatting
- [ ] **Release workflow** — Automated releases
- [ ] **Security scanning** — Vulnerability detection
- [ ] **Dependency updates** — Automated dependency management

### Quality Gates

- [ ] **All tests pass** — No failing tests
- [ ] **Lint passes** — No lint errors
- [ ] **Format passes** — Code is properly formatted
- [ ] **Build succeeds** — Project builds successfully
- [ ] **No security issues** — No known vulnerabilities

## Testing

### Test Setup

- [ ] **Test framework configured** — Jest, pytest, go test, etc.
- [ ] **Test files organized** — Clear test structure
- [ ] **Test fixtures** — Test data and mocks
- [ ] **Test documentation** — How to write tests

### Test Coverage

- [ ] **Unit tests** — Individual function tests
- [ ] **Integration tests** — Component interaction tests
- [ ] **E2E tests** — End-to-end tests (if applicable)
- [ ] **Coverage reporting** — Track test coverage
- [ ] **Coverage thresholds** — Minimum coverage requirements

### Test Quality

- [ ] **Descriptive names** — Clear test descriptions
- [ ] **Independent tests** — Tests don't depend on each other
- [ ] **Fast tests** — Tests run quickly
- [ ] **Reliable tests** — No flaky tests
- [ ] **Edge cases** — Test boundary conditions

## Developer Experience

### Setup

- [ ] **Clear prerequisites** — Required tools and versions
- [ ] **One-command setup** — Simple development setup
- [ ] **Environment variables** — Documented configuration
- [ ] **IDE configuration** — Recommended settings/extensions

### Workflow

- [ ] **Branch naming** — Clear branch conventions
- [ ] **Commit conventions** — Standardized commit messages
- [ ] **PR guidelines** — Pull request best practices
- [ ] **Code review process** — Review expectations

### Tooling

- [ ] **Linter configured** — ESLint, flake8, golangci-lint, etc.
- [ ] **Formatter configured** — Prettier, black, gofmt, etc.
- [ ] **EditorConfig** — Consistent editor settings
- [ ] **Pre-commit hooks** — Automated checks before commit

## Security

### Security Policy

- [ ] **SECURITY.md** — Security policy document
- [ ] **Vulnerability reporting** — How to report security issues
- [ ] **Response timeline** — Expected response times

### Security Practices

- [ ] **No hardcoded secrets** — No API keys, passwords, etc.
- [ ] **Dependency scanning** — Check for vulnerable dependencies
- [ ] **Secret scanning** — Detect secrets in code
- [ ] **Input validation** — Validate all user input
- [ ] **Authentication** — Proper auth implementation
- [ ] **Authorization** — Proper permission checks

### Security Tools

- [ ] **Dependabot/Snyk** — Automated dependency updates
- [ ] **CodeQL** — Static analysis
- [ ] **Secret scanning** — GitHub secret scanning
- [ ] **Security audits** — Regular security reviews

## Release Management

### Versioning

- [ ] **Semantic versioning** — Clear versioning strategy
- [ ] **Version tracking** — Version in package.json, etc.
- [ ] **Release tags** — Git tags for releases

### Release Process

- [ ] **Release checklist** — Steps for releasing
- [ ] **Release notes** — Changelog generation
- [ ] **Automated releases** — CI/CD release workflow
- [ ] **Package publishing** — npm, PyPI, etc.

### Post-Release

- [ ] **Verification** — Verify release works
- [ ] **Announcement** — Announce new releases
- [ ] **Documentation updates** — Update docs for new version

## Accessibility

### Web Applications

- [ ] **Semantic HTML** — Proper HTML structure
- [ ] **ARIA labels** — Accessible labels
- [ ] **Keyboard navigation** — Full keyboard support
- [ ] **Color contrast** — Sufficient contrast ratios
- [ ] **Screen reader support** — Screen reader testing
- [ ] **Focus management** — Proper focus handling

### Documentation

- [ ] **Clear headings** — Proper heading hierarchy
- [ ] **Alt text** — Image descriptions
- [ ] **Link text** — Descriptive link text
- [ ] **Color independence** — Not relying solely on color

## Performance

### Web Applications

- [ ] **Page load time** — Fast initial load
- [ ] **Bundle size** — Optimized bundle
- [ ] **Lazy loading** — Load resources on demand
- [ ] **Caching** — Proper caching strategy
- [ ] **CDN usage** — Static asset delivery

### APIs

- [ ] **Response time** — Fast API responses
- [ ] **Pagination** — Proper pagination
- [ ] **Rate limiting** — Prevent abuse
- [ ] **Caching** — API response caching

## Monitoring & Observability

### Logging

- [ ] **Structured logging** — JSON logs
- [ ] **Log levels** — Appropriate log levels
- [ ] **Error logging** — Capture errors
- [ ] **Performance logging** — Track performance

### Metrics

- [ ] **Key metrics** — Track important metrics
- [ ] **Dashboards** — Visualize metrics
- [ ] **Alerts** — Notify on issues

### Error Tracking

- [ ] **Error capture** — Capture errors
- [ ] **Error reporting** — Report errors
- [ ] **Error resolution** — Fix errors

## Scoring

### Documentation (25%)

| Item | Points |
|------|--------|
| README.md exists | 40 |
| CONTRIBUTING.md exists | 15 |
| CODE_OF_CONDUCT.md exists | 10 |
| SECURITY.md exists | 10 |
| SUPPORT.md exists | 10 |
| CHANGELOG.md exists | 10 |
| LICENSE exists | 5 |

### GitHub Community (20%)

| Item | Points |
|------|--------|
| Issue templates exist | 30 |
| PR template exists | 20 |
| CODEOWNERS exists | 15 |
| Labels configured | 15 |
| Discussions enabled | 10 |
| FUNDING.yml exists | 10 |

### CI/CD (15%)

| Item | Points |
|------|--------|
| Build workflow | 25 |
| Test workflow | 25 |
| Lint workflow | 25 |
| Release workflow | 25 |

### Testing (15%)

| Item | Points |
|------|--------|
| Test framework configured | 30 |
| Test files exist | 30 |
| CI runs tests | 25 |
| Coverage configured | 15 |

### Developer Experience (15%)

| Item | Points |
|------|--------|
| Setup instructions | 30 |
| Development guide | 25 |
| Coding standards | 20 |
| Commit conventions | 15 |
| Debugging guide | 10 |

### Security (10%)

| Item | Points |
|------|--------|
| SECURITY.md exists | 30 |
| Dependency scanning | 25 |
| Secret scanning | 25 |
| No hardcoded secrets | 20 |

### Overall Score

```
Overall = (Documentation × 0.25) + 
          (GitHub Community × 0.20) + 
          (CI/CD × 0.15) + 
          (Testing × 0.15) + 
          (Developer Experience × 0.15) + 
          (Security × 0.10)
```

### Score Interpretation

| Score | Status | Meaning |
|-------|--------|---------|
| 90-100 | ✅ Excellent | Ready for open source |
| 70-89 | ⚠️ Good | Minor improvements needed |
| 50-69 | ⚠️ Fair | Significant improvements needed |
| 0-49 | ❌ Poor | Major work required |

## Priority Matrix

### High Priority (Immediate)

- README.md
- CONTRIBUTING.md
- LICENSE
- Basic CI/CD (build + test)
- Security policy

### Medium Priority (Next Sprint)

- Issue templates
- PR template
- Comprehensive testing
- Documentation improvements
- Developer guide

### Low Priority (Future)

- Advanced CI/CD
- Performance optimization
- Accessibility improvements
- Advanced security features
- Community features

## Usage

### Quick Assessment

1. Check each item in this checklist
2. Calculate scores for each dimension
3. Calculate overall score
4. Identify gaps
5. Create improvement plan

### Detailed Assessment

1. Use the Audit Agent from `agents/audit.md`
2. Generate comprehensive readiness report
3. Prioritize recommendations
4. Create improvement roadmap

### Continuous Improvement

1. Re-assess after each improvement
2. Track progress over time
3. Update checklist as project evolves
4. Celebrate improvements!

---

*This checklist is part of the oss-ready skill.*
