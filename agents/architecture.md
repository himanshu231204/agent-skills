# Architecture Agent

Generate project architecture documentation.

## Purpose

Analyze the repository structure and generate clear architecture documentation. Create diagrams, explain module relationships, and document design decisions.

## Input

- Repository analysis from `agents/audit.md`
- Source code structure
- Configuration files

## Output

ARCHITECTURE.md written to the repository root.

## Documentation Structure

### Overview
- Project type and purpose
- High-level architecture diagram (Mermaid)
- Key design principles

### Directory Structure
- Actual directory tree from the repository
- Description of each major directory
- Purpose of key files

### Key Components
- Each major module with:
  - Responsibilities
  - Key files
  - Dependencies on other modules

### Data Flow
- Request/response flow (sequence diagram)
- Data model (class diagram if applicable)
- Communication patterns between components

### Design Decisions
- Why this framework?
- Why this architecture pattern?
- Why this database?
- Trade-offs made

### Dependencies
- Production dependencies with purpose
- Development dependencies with purpose

### Suggested Improvements
- High priority architectural improvements
- Medium priority improvements
- Low priority improvements

## Generation Rules

### Always Do
- Analyze actual code structure
- Document real relationships
- Reference actual files
- Include working Mermaid diagrams
- Explain design decisions with rationale

### Never Do
- Invent architecture that doesn't exist
- Use placeholder diagrams
- Skip the analysis phase
- Generate generic documentation
