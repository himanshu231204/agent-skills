# Report Agent

Generate the final Open Source Readiness Report.

## Purpose

Synthesize all analysis results into a comprehensive readiness report. Provide scores, recommendations, and next steps for improving the repository.

## Input

- Audit results from `agents/audit.md`
- Generated artifacts list
- Scoring methodology from `reference.md`

## Output

A readiness report following the exact output format defined in `reference.md`.

## Report Structure

1. **Header** — Repository name, timestamp, overall score
2. **Project Overview** — Type, language, framework, package manager, build system, license
3. **Readiness Scores** — Six dimensions with scores, weights, weighted values, and status
4. **Detailed Assessment** — Per-dimension breakdown with item-level status
5. **Generated Artifacts** — Created, improved, and skipped items
6. **Recommendations** — Prioritized by impact (high/medium/low)
7. **Next Steps** — Immediate, short-term, long-term actions
8. **Technology Stack** — Detected tools and versions
9. **Repository Statistics** — Stars, forks, contributors, issues, releases

## Scoring

Use the scoring methodology from `reference.md`. Calculate:
- Per-dimension scores (0-100)
- Weighted scores using defined weights
- Overall weighted average

## Score Interpretation

| Score | Status |
|-------|--------|
| 90-100 | Excellent — Ready for open source |
| 70-89 | Good — Minor improvements needed |
| 50-69 | Fair — Significant improvements needed |
| 0-49 | Poor — Major work required |

## Generation Rules

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
