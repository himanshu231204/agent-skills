# Report Agent

Generate the final Open Source Readiness Report.

## Purpose

The Report Agent synthesizes all analysis results into a comprehensive readiness report. It provides scores, recommendations, and next steps for improving the repository.

## When to Use

- After completing the audit
- After generating artifacts
- When presenting results to the user
- When documenting progress

## Report Format

```markdown
# Open Source Readiness Report

**Repository**: {name}
**Analyzed**: {timestamp}
**Overall Score**: {score}/100

---

## Executive Summary

{2-3 sentence summary of the repository's open source readiness status}

**Key Findings**:
- {Finding 1}
- {Finding 2}
- {Finding 3}

**Top Recommendations**:
1. {Recommendation 1}
2. {Recommendation 2}
3. {Recommendation 3}

---

## Readiness Scores

| Dimension | Score | Weight | Weighted | Status |
|-----------|-------|--------|----------|--------|
| Documentation | X/100 | 25% | X | ✅/⚠️/❌ |
| GitHub Community | X/100 | 20% | X | ✅/⚠️/❌ |
| CI/CD | X/100 | 15% | X | ✅/⚠️/❌ |
| Testing | X/100 | 15% | X | ✅/⚠️/❌ |
| Developer Experience | X/100 | 15% | X | ✅/⚠️/❌ |
| Security | X/100 | 10% | X | ✅/⚠️/❌ |
| **Overall** | | | **X/100** | |

### Score Interpretation

| Score | Status | Meaning |
|-------|--------|---------|
| 90-100 | ✅ Excellent | Ready for open source |
| 70-89 | ⚠️ Good | Minor improvements needed |
| 50-69 | ⚠️ Fair | Significant improvements needed |
| 0-49 | ❌ Poor | Major work required |

---

## Detailed Assessment

### Documentation

**Score**: X/100

| Item | Status | Notes |
|------|--------|-------|
| README.md | ✅/⚠️/❌ | {notes} |
| CONTRIBUTING.md | ✅/⚠️/❌ | {notes} |
| CODE_OF_CONDUCT.md | ✅/⚠️/❌ | {notes} |
| SECURITY.md | ✅/⚠️/❌ | {notes} |
| SUPPORT.md | ✅/⚠️/❌ | {notes} |
| CHANGELOG.md | ✅/⚠️/❌ | {notes} |
| LICENSE | ✅/⚠️/❌ | {notes} |
| API Documentation | ✅/⚠️/❌ | {notes} |
| Code Comments | ✅/⚠️/❌ | {notes} |

### GitHub Community

**Score**: X/100

| Item | Status | Notes |
|------|--------|-------|
| Issue Templates | ✅/⚠️/❌ | {notes} |
| PR Template | ✅/⚠️/❌ | {notes} |
| CODEOWNERS | ✅/⚠️/❌ | {notes} |
| Labels | ✅/⚠️/❌ | {notes} |
| Discussions | ✅/⚠️/❌ | {notes} |
| FUNDING.yml | ✅/⚠️/❌ | {notes} |

### CI/CD

**Score**: X/100

| Workflow | Status | Purpose |
|----------|--------|---------|
| Build | ✅/⚠️/❌ | {purpose} |
| Test | ✅/⚠️/❌ | {purpose} |
| Lint | ✅/⚠️/❌ | {purpose} |
| Release | ✅/⚠️/❌ | {purpose} |
| Security | ✅/⚠️/❌ | {purpose} |
| Dependencies | ✅/⚠️/❌ | {purpose} |

### Testing

**Score**: X/100

| Metric | Value |
|--------|-------|
| Framework | {framework} |
| Test Files | {count} |
| Coverage Config | ✅/❌ |
| CI Integration | ✅/❌ |
| Test Documentation | ✅/❌ |

### Developer Experience

**Score**: X/100

| Item | Status | Notes |
|------|--------|-------|
| Setup Instructions | ✅/⚠️/❌ | {notes} |
| Development Guide | ✅/⚠️/❌ | {notes} |
| Coding Standards | ✅/⚠️/❌ | {notes} |
| Commit Conventions | ✅/⚠️/❌ | {notes} |
| Debugging Guide | ✅/⚠️/❌ | {notes} |
| IDE Configuration | ✅/⚠️/❌ | {notes} |

### Security

**Score**: X/100

| Item | Status | Notes |
|------|--------|-------|
| SECURITY.md | ✅/❌ | {notes} |
| Dependency Scanning | ✅/❌ | {notes} |
| Secret Scanning | ✅/❌ | {notes} |
| No Hardcoded Secrets | ✅/❌ | {notes} |

---

## Generated Artifacts

### Created

- ✅ {artifact1} — {description}
- ✅ {artifact2} — {description}
- ✅ {artifact3} — {description}

### Improved

- ⚠️ {artifact1} — {what was improved}
- ⚠️ {artifact2} — {what was improved}

### Skipped

- ❌ {artifact1} — {reason}
- ❌ {artifact2} — {reason}

---

## Recommendations

### High Priority (Immediate)

1. **{Recommendation}**
   - Impact: {impact}
   - Effort: {effort}
   - Files: {files}

2. **{Recommendation}**
   - Impact: {impact}
   - Effort: {effort}
   - Files: {files}

### Medium Priority (Next Sprint)

1. **{Recommendation}**
   - Impact: {impact}
   - Effort: {effort}
   - Files: {files}

2. **{Recommendation}**
   - Impact: {impact}
   - Effort: {effort}
   - Files: {files}

### Low Priority (Future)

1. **{Recommendation}**
   - Impact: {impact}
   - Effort: {effort}
   - Files: {files}

---

## Next Steps

### Immediate (This Week)

1. {step}
2. {step}
3. {step}

### Short-term (This Month)

1. {step}
2. {step}
3. {step}

### Long-term (This Quarter)

1. {step}
2. {step}
3. {step}

---

## Contribution Opportunities

### Good First Issues

- {issue1} — {description}
- {issue2} — {description}
- {issue3} — {description}

### Documentation Needs

- {need1}
- {need2}
- {need3}

### Testing Gaps

- {gap1}
- {gap2}
- {gap3}

---

## Appendix

### Technology Stack

| Category | Technology |
|----------|------------|
| Language | {language} |
| Framework | {framework} |
| Package Manager | {package_manager} |
| Build System | {build_system} |
| Test Framework | {test_framework} |
| Linter | {linter} |
| Formatter | {formatter} |

### Repository Statistics

| Metric | Value |
|--------|-------|
| Stars | {count} |
| Forks | {count} |
| Contributors | {count} |
| Open Issues | {count} |
| Open PRs | {count} |
| Last Commit | {date} |
| First Commit | {date} |
| Releases | {count} |

---

*Report generated by oss-ready skill*
*Last updated: {timestamp}*
```

## Scoring Methodology

### Overall Score Calculation

```
Overall = (Documentation × 0.25) + 
          (GitHub Community × 0.20) + 
          (CI/CD × 0.15) + 
          (Testing × 0.15) + 
          (Developer Experience × 0.15) + 
          (Security × 0.10)
```

### Status Classification

- **✅ Excellent (90-100)**: Ready for open source release
- **⚠️ Good (70-89)**: Minor improvements needed
- **⚠️ Fair (50-69)**: Significant improvements needed
- **❌ Poor (0-49)**: Major work required

## Report Generation Rules

### Always Do

- Include actual scores from analysis
- Reference specific files and configurations
- Provide actionable recommendations
- Include realistic timelines
- Show progress from previous state (if applicable)

### Never Do

- Inflate scores
- Provide vague recommendations
- Skip the analysis phase
- Generate generic reports

## Instructions

1. Compile all analysis results
2. Calculate scores using the methodology
3. Generate the report in the specified format
4. Prioritize recommendations by impact
5. Provide clear next steps
6. Write the report
