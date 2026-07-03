# GitHub Community Agent

Generate or improve GitHub community files.

## Purpose

The GitHub Community Agent creates the files and configurations that make a repository welcoming to contributors on GitHub. It generates issue templates, PR templates, CODEOWNERS, and other community health files.

## When to Use

- When issue templates are missing
- When PR template is missing
- When CODEOWNERS is missing
- When GitHub labels need configuration
- When discussion categories need setup

## GitHub Community Files

### Issue Templates

#### Bug Report Template

```markdown
---
name: Bug Report
about: Report a bug to help us improve
title: '[BUG] '
labels: bug, triage
assignees: ''
---

## Describe the Bug

A clear and concise description of what the bug is.

## To Reproduce

Steps to reproduce the behavior:

1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior

A clear and concise description of what you expected to happen.

## Screenshots

If applicable, add screenshots to help explain your problem.

## Environment

- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Browser: [e.g., Chrome 120, Firefox 121] (if applicable)
- Version: [e.g., 1.0.0]

## Additional Context

Add any other context about the problem here.
```

#### Feature Request Template

```markdown
---
name: Feature Request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Is your feature request related to a problem?

A clear and concise description of what the problem is.
Ex. "I'm always frustrated when..."

## Describe the Solution You'd Like

A clear and concise description of what you want to happen.

## Describe Alternatives You've Considered

A clear and concise description of any alternative solutions or features you've considered.

## Additional Context

Add any other context or screenshots about the feature request here.
```

#### Documentation Template

```markdown
---
name: Documentation
about: Suggest documentation improvements
title: '[DOCS] '
labels: documentation
assignees: ''
---

## What documentation is affected?

- [ ] README.md
- [ ] CONTRIBUTING.md
- [ ] API Documentation
- [ ] Code Comments
- [ ] Other: _____

## Describe the Issue

A clear description of what documentation is missing or incorrect.

## Suggested Improvement

How should the documentation be improved?

## Additional Context

Add any other context about the documentation issue here.
```

#### Good First Issue Template

```markdown
---
name: Good First Issue
about: Create a good first issue for new contributors
title: '[GOOD FIRST ISSUE] '
labels: good first issue, help wanted
assignees: ''
---

## Description

A clear description of the task.

## Why This is a Good First Issue

- [ ] Well-defined scope
- [ ] No complex dependencies
- [ ] Clear acceptance criteria
- [ ] Documentation available

## Acceptance Criteria

- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

## Suggested Files

- `path/to/file1.js` — What to change
- `path/to/file2.js` — What to change

## Resources

- Related documentation: {link}
- Example implementation: {link}
```

### Pull Request Template

```markdown
## Description

A clear and concise description of what this PR does.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)
- [ ] Test update
- [ ] CI/CD update

## Related Issues

Closes #(issue_number)

## How Has This Been Tested?

Describe the tests that you ran to verify your changes.

- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing performed

## Checklist

- [ ] My code follows the project's coding standards
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules

## Screenshots (if applicable)

Add screenshots to demonstrate visual changes.

## Additional Notes

Add any other notes about the PR here.
```

### CODEOWNERS

```markdown
# CODEOWNERS
# This file defines code ownership for the repository.
# See: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners

# Default owners for everything
* @maintainer-username

# Documentation
*.md @maintainer-username
docs/ @maintainer-username

# Source code
src/ @maintainer-username

# Tests
test/ @maintainer-username
tests/ @maintainer-username

# CI/CD
.github/ @maintainer-username

# Configuration
*.config.* @maintainer-username
package.json @maintainer-username
```

### GitHub Labels

Recommended labels for the repository:

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | #d73a4a | Something isn't working |
| `enhancement` | #a2eeef | New feature or request |
| `documentation` | #0075ca | Improvements or additions to documentation |
| `good first issue` | #7057ff | Good for newcomers |
| `help wanted` | #008672 | Extra attention is needed |
| `question` | #d876e3 | Further information is requested |
| `wontfix` | #ffffff | This will not be worked on |
| `duplicate` | #cfd3d7 | This issue or pull request already exists |
| `invalid` | #e4e669 | This doesn't seem right |
| `priority: high` | #b60205 | High priority |
| `priority: medium` | #fbca04 | Medium priority |
| `priority: low` | #0e8a16 | Low priority |
| `status: in progress` | #ededed | Currently being worked on |
| `status: needs review` | #ededed | Needs review from maintainers |
| `status: blocked` | #d93f0b | Blocked by dependency or decision |

### Discussion Categories

Recommended categories for GitHub Discussions:

| Category | Purpose |
|----------|---------|
| 📣 Announcements | Official project announcements |
| 💬 General | General discussion |
| 💡 Ideas | Ideas and feature requests |
| 🙋 Q&A | Questions and answers |
| 📝 Documentation | Documentation improvements |
| 🐛 Bugs | Bug reports |
| 🎉 Show and Tell | Share what you've built |
| 📦 Releases | Release notes and discussion |

### FUNDING.yml

```yaml
# .github/FUNDING.yml
# These are supported funding model platforms

github: [username]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: ['https://example.com/sponsor']
```

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

## Instructions

1. Check for existing GitHub community files
2. Analyze the repository structure
3. Generate missing files with repository-specific content
4. Customize templates for this technology stack
5. Write files to `.github/` directory
