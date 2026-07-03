# Roadmap Agent

Generate project roadmap documentation.

## Purpose

The Roadmap Agent creates a project roadmap based on the repository's current state, existing issues, and development patterns. It generates a realistic, actionable roadmap that reflects the project's actual direction.

## When to Use

- When ROADMAP.md is missing
- When planning project direction
- When communicating priorities to contributors
- When aligning team efforts

## Roadmap Documentation

### Roadmap Structure

```markdown
# Roadmap

## Current Status

**Version**: {current_version}
**Last Updated**: {date}
**Phase**: {phase_name}

## Vision

{One-sentence vision for the project}

## Goals

### Short-term (1-3 months)

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

### Medium-term (3-6 months)

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

### Long-term (6-12 months)

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Milestones

### v{next_version} — {Milestone Name}

**Target Date**: {date}
**Status**: {planned/in-progress/completed}

**Features**:
- [ ] Feature 1
- [ ] Feature 2

**Improvements**:
- [ ] Improvement 1
- [ ] Improvement 2

### v{next_version + 1} — {Milestone Name}

{Same structure}

## How to Contribute

### High Priority

Issues labeled `priority: high`:
- {issue link} — {description}
- {issue link} — {description}

### Medium Priority

Issues labeled `priority: medium`:
- {issue link} — {description}

### Good First Issues

Issues labeled `good first issue`:
- {issue link} — {description}
- {issue link} — {description}

## Completed

### v{version} — {Milestone Name}

**Completed**: {date}

- ✅ Feature 1
- ✅ Feature 2
- ✅ Improvement 1

## Resources

- [Contributing Guide](CONTRIBUTING.md)
- [Architecture](ARCHITECTURE.md)
- [Changelog](CHANGELOG.md)
```

### Roadmap Generation

Analyze the repository to generate a realistic roadmap:

```
□ Current version and release history
□ Open issues and their priorities
□ Recent commit history and patterns
□ Existing documentation
□ Technology stack and constraints
□ Community activity and contributions
```

### Milestone Planning

For each milestone:

1. **Define scope** — What will be included
2. **Estimate timeline** — Realistic completion date
3. **Identify dependencies** — What must be done first
4. **Assign priorities** — What's most important
5. **Set criteria** — How to know when it's done

### Priority Levels

| Priority | Description | Timeline |
|----------|-------------|----------|
| Critical | Must be done | Immediate |
| High | Important | Current milestone |
| Medium | Desired | Next milestone |
| Low | Nice to have | Future |

## Analysis Protocol

### Step 1: Repository Analysis

Analyze:

```
□ Git tags and releases
□ Open issues and PRs
□ Recent commits
□ Existing roadmap (if any)
□ Project goals (from README or docs)
□ Technology constraints
```

### Step 2: Pattern Detection

Detect patterns:

```
□ Release frequency
□ Feature development pace
□ Bug fix frequency
□ Community contribution patterns
□ Maintenance activity
```

### Step 3: Roadmap Generation

Generate realistic milestones based on:

- Current state of the project
- Available resources (maintainers, contributors)
- Technology constraints
- Community needs
- Project goals

## Quality Rules

### Always Do

- Base roadmap on actual project state
- Set realistic timelines
- Include clear success criteria
- Reference existing issues
- Update with current priorities

### Never Do

- Promise features without resources
- Set unrealistic deadlines
- Ignore existing issues
- Generate generic roadmaps
- Skip the analysis phase

## Instructions

1. Analyze the repository's current state
2. Review open issues and priorities
3. Examine release history and patterns
4. Generate realistic milestones
5. Set achievable timelines
6. Write ROADMAP.md
