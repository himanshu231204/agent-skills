# PR Template

Use this template as a starting point. Customize it for your specific project.

---

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
- [ ] Performance improvement
- [ ] Security fix

## Related Issues

Closes #(issue_number)

## How Has This Been Tested?

Describe the tests that you ran to verify your changes.

- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing performed

**Test Environment**:
- OS: [e.g., Windows 11, macOS 14]
- Browser: [e.g., Chrome 120] (if applicable)
- Node.js: [e.g., 20.x] (if applicable)

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

---

## Review Guidelines

### For Reviewers

- [ ] Code is clean and readable
- [ ] Tests are comprehensive
- [ ] Documentation is updated
- [ ] No security issues
- [ ] Performance is acceptable

### For Authors

- Respond to feedback promptly
- Make requested changes in new commits
- Don't force push during review
- Mark conversations as resolved

---

## Template Usage

To use this template:

1. Create a new pull request
2. The template will be automatically populated
3. Fill in all relevant sections
4. Remove sections that don't apply

## Example

```markdown
## Description

Add OAuth2 support for user authentication.

## Type of Change

- [x] New feature (non-breaking change which adds functionality)

## Related Issues

Closes #123

## How Has This Been Tested?

- [x] Unit tests pass
- [x] Integration tests pass
- [x] Manual testing performed

## Checklist

- [x] My code follows the project's coding standards
- [x] I have performed a self-review of my own code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests pass locally with my changes
- [x] Any dependent changes have been merged and published in downstream modules

## Screenshots (if applicable)

![OAuth Flow](https://example.com/oauth-flow.png)

## Additional Notes

This PR adds OAuth2 support for Google and GitHub providers.
```
