# Todo Console App Constitution
<!-- A living document defining the architectural and development principles of the project. -->

## Core Principles

### I. Spec-Driven Development (SDD)
**"If it's not in the spec, it doesn't exist."**
- **Trigger**: All code changes must originate from a requirement in `specs/`.
- **Traceability**: Every feature must trace back to a User Story or Functional Requirement.
- **Verification**: Tests are the executable specification. No feature is complete without a passing test that maps to an FR.

### II. Protocol-First Architecture
**"Define behavior before implementation."**
- **Abstraction**: Use Python `typing.Protocol` to define boundaries between components (e.g., `TaskStorage`, `UserInterface`).
- **Swappability**: Concrete implementations (e.g., `InMemoryStorage` vs `SqliteStorage`) must be interchangeable without modifying the consumer (Service layer).
- **Testing**: Protocols enable easy mocking for unit tests.

### III. Clean Architecture (Strict Layering)
**"Dependencies point one way: inwards."**
- **Layer 1 (Core)**: `src/models/` - Pure data structures, no dependencies.
- **Layer 2 (Business)**: `src/services/` - Logic and rules. Depends ONLY on Models and Protocols.
- **Layer 3 (Interface)**: `src/cli/` - User interaction. Depends on Services.
- **Rule**: The CLI must NEVER import Storage directly. The Model must NEVER import Services.

### IV. Type Safety & Clarity
**"Readability is paramount; ambiguity is unacceptable."**
- **Strict Typing**: 100% Type Hints required for all functional signatures. Use `mypy` strict mode.
- **Documentation**: Public methods/classes must have Google-style docstrings explaining *Args*, *Returns*, and *Raises*.
- **No Magic**: Avoid `*args`, `**kwargs` unless absolutely necessary for decorators/wrappers.

### V. Future-Proofing (Dependency Injection)
**"Hardcoding is technical debt."**
- **Inversion of Control**: Components should receive their dependencies via `__init__`, not create them internally.
- **Example**: `TaskManager(storage=SqliteStorage())` is better than `TaskManager` creating `SqliteStorage` inside itself.
- **Global State**: Minimal usage of global variables. Application state belongs in instances.

## Governance

### Modification Process
- This Constitution supersedes implicit team habits.
- Amendments require a Request for Comment (RFC) and explicit approval.
- Violations found in Code Review must be blocked until resolved.

**Version**: 2.0.0 (Advanced Architecture)
**Ratified**: 2025-12-18
