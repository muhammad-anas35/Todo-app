# Tasks: Todo Console App

**Input**: Design documents from `/specs/todo-console/`
**Prerequisites**: plan.md (completed), spec.md (completed)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `pyproject.toml` with UV configuration and pytest dependency
- [ ] T002 [P] Create `src/__init__.py` and `src/__main__.py` skeleton
- [ ] T003 [P] Create `src/models/__init__.py`
- [ ] T004 [P] Create `src/services/__init__.py`
- [ ] T005 [P] Create `src/cli/__init__.py`
- [ ] T006 [P] Create `tests/__init__.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure needed before features

- [ ] T007 Create Task dataclass in `src/models/task.py` with id, title, description, is_complete
- [ ] T008 Create TaskManager class skeleton in `src/services/task_manager.py` with _tasks dict and _next_id

**Checkpoint**: Foundation ready - feature implementation can begin

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Users can create new tasks with title and description

### Tests for User Story 1

- [ ] T009 [US1] Write test_add_task in `tests/test_task_manager.py`

### Implementation for User Story 1

- [ ] T010 [US1] Implement `add_task(title, description)` method in TaskManager
- [ ] T011 [US1] Add "Add Task" option in CLI menu

**Checkpoint**: Users can add tasks via CLI

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can see all tasks with status indicators

### Tests for User Story 2

- [ ] T012 [US2] Write test_get_all_tasks in `tests/test_task_manager.py`

### Implementation for User Story 2

- [ ] T013 [US2] Implement `get_all_tasks()` method in TaskManager
- [ ] T014 [US2] Add "View Tasks" option with ○/✓ indicators in CLI

**Checkpoint**: Users can view all tasks with status

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status

### Tests for User Story 3

- [ ] T015 [US3] Write test_toggle_complete in `tests/test_task_manager.py`

### Implementation for User Story 3

- [ ] T016 [US3] Implement `toggle_complete(id)` method in TaskManager
- [ ] T017 [US3] Add "Mark Complete/Incomplete" option in CLI

**Checkpoint**: Users can toggle task status

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Users can modify task title and description

### Tests for User Story 4

- [ ] T018 [US4] Write test_update_task in `tests/test_task_manager.py`

### Implementation for User Story 4

- [ ] T019 [US4] Implement `update_task(id, title, description)` method in TaskManager
- [ ] T020 [US4] Add "Update Task" option in CLI

**Checkpoint**: Users can update task details

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks by ID

### Tests for User Story 5

- [ ] T021 [US5] Write test_delete_task in `tests/test_task_manager.py`

### Implementation for User Story 5

- [ ] T022 [US5] Implement `delete_task(id)` method in TaskManager
- [ ] T023 [US5] Add "Delete Task" option in CLI

**Checkpoint**: All 5 core features complete

---

## Phase 8: Polish & Documentation

**Purpose**: Final touches and documentation

- [ ] T024 [P] Create `README.md` with setup and usage instructions
- [ ] T025 [P] Write `tests/test_task.py` for Task model
- [ ] T026 Run all tests and verify passing
- [ ] T027 Manual testing of full workflow

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies
- **Phase 2 (Foundational)**: Depends on Phase 1
- **Phases 3-7 (User Stories)**: Depend on Phase 2, can run sequentially by priority
- **Phase 8 (Polish)**: Depends on all features complete

### Parallel Opportunities

- T002-T006 can all run in parallel (different files)
- T024-T025 can run in parallel with each other
- Within each user story: test → implement → CLI (sequential)

---

## Notes

- Tests written before implementation (TDD)
- Commit after each task/phase
- All operations must handle "Task not found" gracefully
- CLI should validate numeric input for IDs
