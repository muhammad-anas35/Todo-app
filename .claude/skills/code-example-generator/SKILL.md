---
name: code-example-generator
version: 1.0.0
description: Specialized skill for generating idiomatic, type-safe, and documented Python code examples.
---

## Capabilities

### 1. Type Safety First
- **Rule**: All generated examples MUST have type hints.
- **Standard**: Python 3.10+ syntax (`list[str] | None` instead of `Optional[List[str]]`).

### 2. Context Awareness
- **Input**: Takes the current file structure as context.
- **Output**: Generates code that fits existing patterns (e.g., using `dataclasses` for models).

### 3. Documentation
- **Rule**: Every function in an example must have a docstring.
- **Style**: Google Style (Args, Returns).

## Templates

### Storage Implementation
```python
class {Name}Storage:
    """Implementation of TaskStorage using {Tech}."""

    def __init__(self, path: str) -> None:
        self.path = path

    def get_all(self) -> list[Task]:
        # Implementation...
```
