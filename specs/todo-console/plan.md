# Implementation Plan: Todo Console App

**Branch**: `main` | **Date**: 2025-12-08 | **Spec**: [spec.md](file:///d:/Coding%20world/Hackathon_2/project_2/specs/todo-console/spec.md)
**Input**: Feature specification from `/specs/todo-console/spec.md`

## Summary

Build a command-line todo application in Python that stores tasks in memory. The app provides 5 core features: Add, View, Update, Delete, and Mark Complete/Incomplete tasks via an interactive menu.

## Technical Context

**Language/Version**: Python 3.13+  
**Primary Dependencies**: None (stdlib only)  
**Package Manager**: UV  
**Storage**: In-memory (Python list/dict)  
**Testing**: pytest  
**Target Platform**: Windows/Linux/macOS CLI  
**Project Type**: Single project (CLI app)  
**Performance Goals**: Instant response for all operations  
**Constraints**: No persistence - data lost on exit  
**Scale/Scope**: Single user, local execution

## Constitution Check

✅ **In-Memory First**: Data stored in memory only  
✅ **Clean CLI Interface**: Interactive menu with status indicators  
✅ **Type Safety**: Type hints on all functions  
✅ **Single Responsibility**: Models, services, CLI separation  
✅ **Simplicity**: YAGNI - only 5 required features

## Project Structure

### Documentation (this feature)

```text
specs/todo-console/
├── spec.md              # Feature specification (created)
├── plan.md              # This file
└── tasks.md             # Task breakdown (to create)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── __main__.py          # Entry point
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass
├── services/
│   ├── __init__.py
│   └── task_manager.py  # Business logic (CRUD)
└── cli/
    ├── __init__.py
    └── menu.py          # Interactive menu

tests/
├── __init__.py
├── test_task.py         # Model tests
└── test_task_manager.py # Service tests
```

**Structure Decision**: Single project with `src/` layout, standard Python package structure with UV.

---

## Proposed Changes

### 1. Project Configuration

#### [NEW] [pyproject.toml](file:///d:/Coding%20world/Hackathon_2/project_2/pyproject.toml)

UV project configuration with:
- Python 3.13+ requirement
- pytest as dev dependency
- Entry point: `todo-console = "src.__main__:main"`

---

### 2. Models

#### [NEW] [task.py](file:///d:/Coding%20world/Hackathon_2/project_2/src/models/task.py)

Task dataclass with:
- `id: int` - Unique identifier
- `title: str` - Task title (required)
- `description: str` - Task description (optional, default "")
- `is_complete: bool` - Completion status (default False)

---

### 3. Services

#### [NEW] [task_manager.py](file:///d:/Coding%20world/Hackathon_2/project_2/src/services/task_manager.py)

TaskManager class with:
- `_tasks: dict[int, Task]` - In-memory storage
- `_next_id: int` - Auto-increment counter
- `add_task(title, description) -> Task`
- `get_all_tasks() -> list[Task]`
- `get_task(id) -> Task | None`
- `update_task(id, title, description) -> bool`
- `delete_task(id) -> bool`
- `toggle_complete(id) -> bool`

---

### 4. CLI

#### [NEW] [menu.py](file:///d:/Coding%20world/Hackathon_2/project_2/src/cli/menu.py)

Interactive menu with options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

---

### 5. Entry Point

#### [NEW] [__main__.py](file:///d:/Coding%20world/Hackathon_2/project_2/src/__main__.py)

Main entry point that:
- Creates TaskManager instance
- Runs menu loop
- Handles keyboard interrupt (Ctrl+C)

---

### 6. Documentation

#### [NEW] [README.md](file:///d:/Coding%20world/Hackathon_2/project_2/README.md)

Setup and usage instructions including:
- Prerequisites (Python 3.13+, UV)
- Installation steps
- How to run the app
- Feature list

---

## Verification Plan

### Automated Tests

**Command**: `uv run pytest tests/ -v`

| Test File | What It Tests |
|-----------|---------------|
| `tests/test_task.py` | Task model creation, defaults, attributes |
| `tests/test_task_manager.py` | All CRUD operations, edge cases, error handling |

**Test Coverage**:
1. Add task with/without description
2. Get all tasks (empty, with items)
3. Update task (valid ID, invalid ID)
4. Delete task (valid ID, invalid ID)
5. Toggle complete (valid ID, invalid ID)

### Manual Verification

**Run the app**: `uv run python -m src`

**Test Scenario**:
1. Start app → See menu with 6 options
2. Select "1" → Enter title "Buy groceries" → Enter description "Milk, eggs" → See "Task added with ID 1"
3. Select "2" → See task list with "○ [1] Buy groceries - Milk, eggs"
4. Select "5" → Enter ID "1" → See "Task marked complete"
5. Select "2" → See "✓ [1] Buy groceries - Milk, eggs"
6. Select "3" → Enter ID "1" → Enter new title "Go shopping" → See "Task updated"
7. Select "4" → Enter ID "1" → See "Task deleted"
8. Select "2" → See "No tasks found"
9. Select "6" → App exits

---

## Complexity Tracking

No constitution violations - following all principles.
