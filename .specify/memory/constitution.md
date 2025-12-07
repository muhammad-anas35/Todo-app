# Todo Console App Constitution

## Core Principles

### I. In-Memory First
All task data is stored in memory during runtime. No file or database persistence - data is ephemeral and lost on exit. This keeps the app simple and focused on core CRUD operations.

### II. Clean CLI Interface
The application exposes functionality via an interactive command-line interface. Users interact through numbered menus and prompts. All output is human-readable with clear status indicators (✓/○).

### III. Type Safety
Use Python type hints throughout the codebase. All function parameters and return types must be explicitly typed. This improves code readability and enables static analysis.

### IV. Single Responsibility
Each module has one clear purpose:
- `models/` - Data structures (Task entity)
- `services/` - Business logic (TaskManager)
- `cli/` - User interface (menu, prompts)

### V. Test-First Development
TDD is mandatory: Write tests first → Verify they fail → Implement → Verify they pass → Refactor. Red-Green-Refactor cycle strictly enforced.

### VI. Simplicity Over Features
Start simple, follow YAGNI (You Aren't Gonna Need It). No over-engineering. Only implement what's explicitly required in the specification.

## Technology Stack

- **Language**: Python 3.13+
- **Package Manager**: UV
- **Testing**: pytest
- **Linting**: ruff
- **Type Checking**: mypy (optional)

## Project Structure

```
project_2/
├── .specify/           # Spec-Kit Plus configuration
├── specs/              # Feature specifications
├── history/            # Prompt History Records
├── src/                # Source code
│   ├── models/         # Data models
│   ├── services/       # Business logic
│   └── cli/            # CLI interface
├── tests/              # Test files
├── pyproject.toml      # Project configuration
├── README.md           # Setup instructions
└── GEMINI.md           # AI assistant rules
```

## Governance

This constitution supersedes all other practices. Amendments require documentation and approval. All code must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-08 | **Last Amended**: 2025-12-08
