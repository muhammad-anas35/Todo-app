"""Tests for the TaskManager service."""

import pytest

from src.models.task import Task
from src.services.task_manager import TaskManager, InMemoryStorage


class TestTaskManagerAddTask:
    """Tests for adding tasks."""
    
    def test_add_task_returns_task(self) -> None:
        """Adding a task returns the created Task."""
        manager = TaskManager()
        
        task = manager.add_task("Test Task", "Description")
        
        assert isinstance(task, Task)
        assert task.title == "Test Task"
        assert task.description == "Description"
        assert task.is_complete is False
    
    def test_add_task_assigns_incremental_ids(self) -> None:
        """Tasks get incrementing IDs."""
        manager = TaskManager()
        
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        task3 = manager.add_task("Task 3")
        
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
    
    def test_add_task_without_description(self) -> None:
        """Task can be added without description."""
        manager = TaskManager()
        
        task = manager.add_task("Only Title")
        
        assert task.title == "Only Title"
        assert task.description == ""
    
    def test_add_task_with_empty_title_raises_error(self) -> None:
        """Empty title raises ValueError."""
        manager = TaskManager()
        
        with pytest.raises(ValueError):
            manager.add_task("")


class TestTaskManagerGetTasks:
    """Tests for retrieving tasks."""
    
    def test_get_all_tasks_empty(self) -> None:
        """Getting all tasks from empty manager returns empty list."""
        manager = TaskManager()
        
        tasks = manager.get_all_tasks()
        
        assert tasks == []
    
    def test_get_all_tasks_returns_all(self) -> None:
        """All added tasks are returned."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        
        tasks = manager.get_all_tasks()
        
        assert len(tasks) == 3
    
    def test_get_all_tasks_sorted_by_id(self) -> None:
        """Tasks are returned sorted by ID."""
        manager = TaskManager()
        manager.add_task("First")
        manager.add_task("Second")
        manager.add_task("Third")
        
        tasks = manager.get_all_tasks()
        
        assert [t.id for t in tasks] == [1, 2, 3]
    
    def test_get_task_by_id(self) -> None:
        """Can retrieve specific task by ID."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Target Task", "Find me")
        manager.add_task("Task 3")
        
        task = manager.get_task(2)
        
        assert task is not None
        assert task.title == "Target Task"
        assert task.description == "Find me"
    
    def test_get_task_not_found(self) -> None:
        """Getting non-existent task returns None."""
        manager = TaskManager()
        manager.add_task("Task 1")
        
        task = manager.get_task(999)
        
        assert task is None


class TestTaskManagerUpdateTask:
    """Tests for updating tasks."""
    
    def test_update_task_title(self) -> None:
        """Task title can be updated."""
        manager = TaskManager()
        manager.add_task("Original Title")
        
        result = manager.update_task(1, title="Updated Title")
        
        assert result is True
        task = manager.get_task(1)
        assert task is not None
        assert task.title == "Updated Title"
    
    def test_update_task_description(self) -> None:
        """Task description can be updated."""
        manager = TaskManager()
        manager.add_task("Title", "Original Desc")
        
        result = manager.update_task(1, description="Updated Desc")
        
        assert result is True
        task = manager.get_task(1)
        assert task is not None
        assert task.description == "Updated Desc"
    
    def test_update_task_both_fields(self) -> None:
        """Both title and description can be updated together."""
        manager = TaskManager()
        manager.add_task("Old Title", "Old Desc")
        
        result = manager.update_task(1, title="New Title", description="New Desc")
        
        assert result is True
        task = manager.get_task(1)
        assert task is not None
        assert task.title == "New Title"
        assert task.description == "New Desc"
    
    def test_update_preserves_completion_status(self) -> None:
        """Update preserves is_complete status."""
        manager = TaskManager()
        manager.add_task("Task")
        manager.toggle_complete(1)  # Mark complete
        
        manager.update_task(1, title="Updated")
        
        task = manager.get_task(1)
        assert task is not None
        assert task.is_complete is True
    
    def test_update_task_not_found(self) -> None:
        """Updating non-existent task returns False."""
        manager = TaskManager()
        
        result = manager.update_task(999, title="Nope")
        
        assert result is False


class TestTaskManagerDeleteTask:
    """Tests for deleting tasks."""
    
    def test_delete_task(self) -> None:
        """Task can be deleted by ID."""
        manager = TaskManager()
        manager.add_task("To Delete")
        
        result = manager.delete_task(1)
        
        assert result is True
        assert manager.get_task(1) is None
        assert manager.get_task_count() == 0
    
    def test_delete_task_not_found(self) -> None:
        """Deleting non-existent task returns False."""
        manager = TaskManager()
        manager.add_task("Task 1")
        
        result = manager.delete_task(999)
        
        assert result is False
        assert manager.get_task_count() == 1
    
    def test_delete_task_preserves_others(self) -> None:
        """Deleting one task preserves other tasks."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        
        manager.delete_task(2)
        
        tasks = manager.get_all_tasks()
        assert len(tasks) == 2
        assert [t.id for t in tasks] == [1, 3]


class TestTaskManagerToggleComplete:
    """Tests for toggling completion status."""
    
    def test_toggle_incomplete_to_complete(self) -> None:
        """Incomplete task can be marked complete."""
        manager = TaskManager()
        manager.add_task("Task")
        
        result = manager.toggle_complete(1)
        
        assert result is True
        task = manager.get_task(1)
        assert task is not None
        assert task.is_complete is True
    
    def test_toggle_complete_to_incomplete(self) -> None:
        """Complete task can be marked incomplete."""
        manager = TaskManager()
        manager.add_task("Task")
        manager.toggle_complete(1)  # Now complete
        
        result = manager.toggle_complete(1)  # Toggle back
        
        assert result is True
        task = manager.get_task(1)
        assert task is not None
        assert task.is_complete is False
    
    def test_toggle_task_not_found(self) -> None:
        """Toggling non-existent task returns False."""
        manager = TaskManager()
        
        result = manager.toggle_complete(999)
        
        assert result is False


class TestTaskManagerCounts:
    """Tests for count methods."""
    
    def test_task_count_empty(self) -> None:
        """Empty manager has 0 tasks."""
        manager = TaskManager()
        
        assert manager.get_task_count() == 0
    
    def test_task_count(self) -> None:
        """Task count reflects added tasks."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        
        assert manager.get_task_count() == 2
    
    def test_completed_count_empty(self) -> None:
        """Empty manager has 0 completed tasks."""
        manager = TaskManager()
        
        assert manager.get_completed_count() == 0
    
    def test_completed_count(self) -> None:
        """Completed count reflects completed tasks."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.toggle_complete(1)
        manager.toggle_complete(3)
        
        assert manager.get_completed_count() == 2


class TestInMemoryStorage:
    """Tests for the InMemoryStorage implementation."""
    
    def test_save_and_get(self) -> None:
        """Can save and retrieve tasks."""
        storage = InMemoryStorage()
        task = Task(id=1, title="Test")
        
        storage.save(task)
        retrieved = storage.get_by_id(1)
        
        assert retrieved is not None
        assert retrieved.title == "Test"
    
    def test_delete(self) -> None:
        """Can delete tasks."""
        storage = InMemoryStorage()
        task = Task(id=1, title="Test")
        storage.save(task)
        
        result = storage.delete(1)
        
        assert result is True
        assert storage.get_by_id(1) is None
    
    def test_get_all_sorted(self) -> None:
        """Get all returns tasks sorted by ID."""
        storage = InMemoryStorage()
        storage.save(Task(id=3, title="Third"))
        storage.save(Task(id=1, title="First"))
        storage.save(Task(id=2, title="Second"))
        
        tasks = storage.get_all()
        
        assert [t.id for t in tasks] == [1, 2, 3]
