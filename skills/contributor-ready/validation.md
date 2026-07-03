# Validation Framework

Use these checklists to verify the contributor-ready skill itself is publication-quality.

## Skill Quality Checklist

### Structure

- [ ] `skill.md` is concise and serves as entry point
- [ ] `AGENT.md` defines orchestration without duplicating content
- [ ] `prompt.md` is a clean system prompt referencing other files
- [ ] `reference.md` is the single source of truth for detection, scoring, output format
- [ ] `agents/` contains specialized instructions with clear input/output
- [ ] `templates/` contains consistent, unbiased templates
- [ ] `examples/` covers major technology stacks
- [ ] `validation.md` exists (this file)

### Duplication Check

- [ ] Scoring methodology appears ONLY in `reference.md`
- [ ] Detection tables appear ONLY in `reference.md`
- [ ] Output format appears ONLY in `reference.md`
- [ ] Core rules appear ONLY in `reference.md`
- [ ] No agent file duplicates another agent's content
- [ ] Templates do not duplicate agent instructions

### Conflict Check

- [ ] All files agree on execution order (analyze → score → generate → report)
- [ ] All files agree on safe mode behavior (never overwrite unless requested)
- [ ] All files agree on technology detection (use reference.md tables)
- [ ] All files agree on scoring weights
- [ ] No contradictory instructions between files

### Template Consistency

- [ ] All templates use `{placeholder}` syntax
- [ ] All templates have consistent heading style
- [ ] No templates contain technology-specific assumptions (npm, pip, etc.)
- [ ] No templates contain auto-generated footers
- [ ] All templates are concise and actionable

### Technology Neutrality

- [ ] No file assumes a specific package manager without detection
- [ ] No file assumes a specific CI platform without detection
- [ ] No file assumes a specific language without detection
- [ ] CI/CD examples cover multiple stacks (not just Node.js)
- [ ] Release examples cover multiple package managers

### Modularity

- [ ] Each agent has clear responsibility
- [ ] Each agent documents its input requirements
- [ ] Each agent documents its output format
- [ ] Agents reference `reference.md` instead of duplicating detection logic
- [ ] No circular dependencies between agents

### Publication Quality

- [ ] No AI-generated filler text ("This example demonstrates...")
- [ ] No placeholder content that would confuse users
- [ ] All examples are realistic and practical
- [ ] Writing is clear, concise, and professional
- [ ] File organization is logical and easy to navigate

## Repository Compatibility Checklist

Use this when running contributor-ready on a target repository.

### Detection Verification

- [ ] Primary language detected correctly
- [ ] Framework detected correctly
- [ ] Package manager detected correctly
- [ ] Build system detected correctly
- [ ] Testing framework detected correctly
- [ ] CI/CD platform detected correctly

### Generated Content Verification

- [ ] README uses real project name and description
- [ ] README references actual dependencies
- [ ] README includes correct installation commands
- [ ] README includes working code examples
- [ ] CONTRIBUTING.md uses correct development commands
- [ ] CI workflows use correct language/runtime setup
- [ ] No placeholder text remains in generated files
- [ ] All file paths reference real files in the project

### Quality Verification

- [ ] Generated content is specific to this repository
- [ ] No generic or template-like content
- [ ] Code examples would actually work
- [ ] Instructions are accurate for the detected stack
- [ ] Scoring reflects actual repository state

## Maintenance Checklist

Use this when updating the contributor-ready skill.

### After Adding a New Language

- [ ] Add detection entry to `reference.md` (Languages table)
- [ ] Add framework detection entries if applicable
- [ ] Add package manager detection if applicable
- [ ] Add build system detection if applicable
- [ ] Add testing framework detection if applicable
- [ ] Add technology adaptation row to adaptation table
- [ ] Create example file in `examples/` if warranted

### After Adding a New Framework

- [ ] Add detection entry to `reference.md` (Frameworks table)
- [ ] Add technology adaptation notes if applicable
- [ ] Create example file in `examples/` if warranted

### After Modifying Scoring

- [ ] Update scoring tables in `reference.md`
- [ ] Verify `agents/audit.md` references the updated scoring
- [ ] Verify `agents/report.md` references the updated scoring
- [ ] Verify `checklist.md` scoring matches

### After Modifying Templates

- [ ] Verify all templates use consistent placeholder syntax
- [ ] Verify no technology-specific assumptions were introduced
- [ ] Verify templates are concise and actionable
- [ ] Verify no auto-generated footers exist

### After Modifying Agents

- [ ] Verify input/output contracts are documented
- [ ] Verify no duplication with other agents
- [ ] Verify reference to `reference.md` is correct
- [ ] Verify instructions are clear and actionable
