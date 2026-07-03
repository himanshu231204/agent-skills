# Documentation Agent

Generate or improve repository-specific documentation.

## Purpose

Create high-quality, repository-specific documentation that helps users understand, install, and use the project. Generate only what's missing. Improve existing documentation when requested.

## Input

- Repository analysis from `agents/audit.md`
- Detection results (languages, frameworks, package managers) from `reference.md`
- Templates from `templates/`

## Output

Documentation files written to the repository root or `docs/` directory.

## Files to Generate

### README.md (from `templates/README.md`)

The most important file. Must include:
- Project name and clear description
- Features with benefits
- Prerequisites (language version, package manager, other tools)
- Installation instructions using detected package manager
- Quick start with working code example
- Usage examples with real code
- Configuration (if applicable)
- Contributing link
- License

### CONTRIBUTING.md (from `templates/CONTRIBUTING.md`)

Guide for contributors. Must include:
- Prerequisites
- Development setup (fork, clone, install, branch)
- Development workflow (make changes, run tests, commit)
- Coding standards (detected from project)
- Commit conventions
- Pull request guidelines

### CODE_OF_CONDUCT.md (from `templates/CODE_OF_CONDUCT.md`)

Standard Contributor Covenant. Only customize the contact email.

### SECURITY.md (from `templates/SECURITY.md`)

Security policy. Include:
- Supported versions
- Vulnerability reporting process
- Response timeline
- Security practices

### SUPPORT.md (from `templates/SUPPORT.md`)

How to get help. Include:
- Documentation links
- Community channels
- Bug reporting process
- Feature request process
- FAQ

## Generation Rules

### Always Do
- Use real file paths from the repository
- Reference actual code patterns
- Include working code examples
- Be specific to this technology stack (use adaptation tables from `reference.md`)
- Explain WHY, not just WHAT
- Include expected output when possible

### Never Do
- Use placeholder text
- Invent features the project doesn't have
- Copy generic templates without customization
- Skip the analysis phase
- Assume technology without detection

## Template Customization

For each template:
1. Read the template from `templates/`
2. Analyze the repository for specific content
3. Replace all placeholders with real values
4. Add technology-specific sections using adaptation tables from `reference.md`
5. Verify accuracy before writing
