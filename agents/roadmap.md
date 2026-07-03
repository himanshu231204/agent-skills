# Roadmap Agent

Generate project roadmap documentation.

## Purpose

Create a project roadmap based on the repository's current state, existing issues, and development patterns. Generate a realistic, actionable roadmap that reflects the project's actual direction.

## Input

- Repository analysis from `agents/audit.md`
- Git tags and release history
- Open issues and priorities

## Output

ROADMAP.md written to the repository root.

## Documentation Structure

### Current Status
- Current version and release date
- Current development phase

### Vision
- One-sentence vision for the project

### Goals
- Short-term (1-3 months)
- Medium-term (3-6 months)
- Long-term (6-12 months)

### Milestones
For each milestone:
- Version number and name
- Target date
- Status (planned/in-progress/completed)
- Features, improvements, bug fixes

### How to Contribute
- High priority issues
- Medium priority issues
- Good first issues

### Completed
- Past milestones with completion dates

### Release Schedule
- Upcoming versions with target dates

### Priorities
- What the project is focusing on
- What the project is NOT focusing on (and why)

## Analysis Protocol

1. Analyze git tags and release history for versioning patterns
2. Review open issues and their priorities
3. Examine recent commit history for development pace
4. Detect community contribution patterns
5. Generate realistic milestones based on available resources

## Generation Rules

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
