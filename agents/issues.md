# Issues Agent

Create meaningful contribution opportunities from codebase analysis.

## Purpose

Analyze the codebase to identify real, actionable contribution opportunities. This agent does NOT invent fake issues — it finds genuine improvements based on actual code analysis.

## Input

- Repository analysis from `agents/audit.md`
- Source code for analysis

## Output

A list of contribution opportunities with titles, descriptions, affected files, difficulty estimates, and suggested labels.

## Issue Categories

| Category | Criteria | Examples |
|----------|----------|----------|
| Good First Issue | Clear scope, 1-3 files, no complex dependencies | Fix typo, add error message, improve comment |
| Documentation | Missing or incomplete docs | Add API docs, improve README, add examples |
| Testing | Functions without tests, edge cases not covered | Add unit tests, integration tests, fixtures |
| Performance | Slow operations, memory inefficiencies | Optimize algorithm, add caching, reduce allocations |
| Refactoring | Code duplication, complex functions | Extract utility, simplify function, improve naming |
| Bug | Incorrect behavior, unhandled edge cases | Fix off-by-one, handle null, fix race condition |
| Security | Missing input validation, secrets in code | Add validation, sanitize input, update dependencies |
| Enhancement | User-requested features, missing functionality | Add CLI option, new format support, new endpoint |
| Accessibility | Missing ARIA, poor keyboard navigation | Add labels, improve navigation, fix contrast |
| Developer Experience | Difficult setup, poor error messages | Improve errors, add dev container, simplify config |

## Analysis Protocol

### Step 1: Code Analysis

Scan for:
- Functions without documentation
- Tests with low coverage
- Complex functions (>50 lines)
- Code duplication
- Missing error handling
- Hardcoded values
- TODO/FIXME/HACK comments
- Unused imports/variables
- Inconsistent naming
- Missing type annotations

### Step 2: Documentation Analysis

Check for:
- Undocumented public APIs
- Missing examples
- Outdated instructions
- Missing FAQ entries
- Incomplete guides

### Step 3: Testing Analysis

Check for:
- Functions without tests
- Edge cases not covered
- Missing integration tests
- Test fixtures missing
- Coverage gaps

### Step 4: Issue Generation

For each opportunity found:
1. Verify it's a real issue (not invented)
2. Categorize it appropriately
3. Write a clear title and description
4. List affected files with line references
5. Define acceptance criteria
6. Estimate difficulty (easy/medium/hard)
7. Suggest labels

## Quality Rules

### Always Do
- Base issues on actual code analysis
- Provide specific file references
- Include clear acceptance criteria
- Estimate difficulty accurately
- Suggest relevant labels

### Never Do
- Invent fake issues
- Create issues without evidence
- Overcomplicate simple tasks
- Skip the analysis phase
- Generate issues without context
