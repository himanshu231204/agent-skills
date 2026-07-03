# GitHub Community Agent

Generate or improve GitHub community files.

## Purpose

Create the files and configurations that make a repository welcoming to contributors on GitHub. Generate issue templates, PR templates, CODEOWNERS, labels, and other community health files.

## Input

- Repository analysis from `agents/audit.md`
- Repository structure and maintainer info

## Output

GitHub community files written to `.github/` directory.

## Files to Generate

### Issue Templates

Create in `.github/ISSUE_TEMPLATE/`:

**Bug Report** (`bug_report.md`):
- Describe the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, version)
- Screenshots (if applicable)

**Feature Request** (`feature_request.md`):
- Problem description
- Desired solution
- Alternatives considered
- Additional context

**Documentation** (`documentation.md`):
- Which documentation is affected
- Describe the issue
- Suggested improvement

### Pull Request Template

Create `.github/PULL_REQUEST_TEMPLATE.md`:
- Description of changes
- Type of change (bug fix, feature, breaking change, docs, refactor, test, CI)
- Related issues
- Testing performed
- Checklist (code standards, self-review, docs updated, tests pass)

### CODEOWNERS

Create `.github/CODEOWNERS`:
- Detect maintainer from git config or ask user
- Map code ownership by directory and file type
- Use `*` as default owner

### Labels

Recommend labels with colors and descriptions:
- `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`
- `priority: high`, `priority: medium`, `priority: low`
- `status: in progress`, `status: needs review`, `status: blocked`

### Discussion Categories

Recommend categories for GitHub Discussions:
- Announcements, General, Ideas, Q&A, Documentation, Bugs, Show and Tell, Releases

### FUNDING.yml

Create `.github/FUNDING.yml` with detected or user-provided sponsorship platforms.

## Generation Rules

### Always Do
- Use real maintainer usernames (detect from git config or ask)
- Reference actual project structure
- Include relevant labels
- Customize templates for this technology stack
- Follow GitHub best practices

### Never Do
- Use placeholder usernames
- Generate templates that don't apply
- Create labels that already exist
- Skip analysis of existing configuration
