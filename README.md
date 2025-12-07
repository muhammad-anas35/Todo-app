# Todo Console App

A command-line todo application that stores tasks in memory, built with Python 3.13+ and UV.

## Features

- ➕ **Add Task** - Create tasks with title and optional description
- 📋 **View Tasks** - List all tasks with status indicators (✓/○)
- ✏️ **Update Task** - Modify task title and description
- 🗑️ **Delete Task** - Remove tasks by ID
- ✓ **Toggle Complete** - Mark tasks as complete/incomplete

## Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) package manager

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd project_2

# Install dependencies with UV
uv sync
```

## Usage

```bash
# Run the application
uv run src

# Or after installation
uv run todo
```

## Project Structure

```
project_2/
├── src/
│   ├── __init__.py
│   ├── __main__.py          # Entry point
│   ├── models/
│   │   └── task.py          # Task dataclass
│   ├── services/
│   │   └── task_manager.py  # CRUD operations
│   └── cli/
│       └── menu.py          # Interactive menu
├── tests/
│   ├── test_task.py
│   └── test_task_manager.py
├── specs/                    # Feature specifications
├── pyproject.toml
└── README.md
```

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ -v --cov=src
```

## Development

This project uses Spec-Driven Development with Spec-Kit Plus. See the `specs/` folder for feature specifications.

### Code Quality

```bash
# Format code
uv run ruff format src/ tests/

# Lint code
uv run ruff check src/ tests/
```

## License

MIT
