"""TaskManager service - Business logic for CRUD operations on tasks.

This module provides the core service layer for managing tasks in memory.
Follows the Single Responsibility Principle - only handles task operations.
"""

from typing import Protocol

from src.models.task import Task


class TaskStorage(Protocol):
    """Protocol for task storage backends (for future extensibility)."""
    
    def save(self, task: Task) -> None:
        """Save a task to storage."""
        ...
    
    def delete(self, task_id: int) -> bool:
        """Delete a task from storage."""
        ...
    
    def get_all(self) -> list[Task]:
        """Get all tasks from storage."""
        ...
    
    def get_by_id(self, task_id: int) -> Task | None:
        """Get a specific task by ID."""
        ...


class InMemoryStorage:
    """In-memory storage implementation using a dictionary.
    
    Tasks are stored with their ID as key for O(1) lookup.
    Data is lost when the application exits.
    """
    
    def __init__(self) -> None:
        """Initialize empty storage."""
        self._tasks: dict[int, Task] = {}
    
    def save(self, task: Task) -> None:
        """Save a task to memory."""
        self._tasks[task.id] = task
    
    def delete(self, task_id: int) -> bool:
        """Delete a task from memory. Returns True if found and deleted."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    def get_all(self) -> list[Task]:
        """Get all tasks, sorted by ID."""
        return sorted(self._tasks.values(), key=lambda t: t.id)
    
    def get_by_id(self, task_id: int) -> Task | None:
        """Get a task by ID, or None if not found."""
        return self._tasks.get(task_id)


class TaskManager:
    """Manages tasks with CRUD operations using pluggable storage.
    
    This is the main service class that coordinates task operations.
    Uses InMemoryStorage by default, but can accept any TaskStorage implementation.
    
    Attributes:
        storage: The storage backend (default: InMemoryStorage)
        
    Example:
        >>> manager = TaskManager()
        >>> task = manager.add_task("Buy groceries", "Milk and eggs")
        >>> task.id
        1
        >>> manager.get_all_tasks()
        [Task(id=1, title='Buy groceries', ...)]
    """
    
    def __init__(self, storage: TaskStorage | None = None) -> None:
        """Initialize TaskManager with optional storage backend.
        
        Args:
            storage: Storage implementation (default: InMemoryStorage)
        """
        self._storage = storage if storage is not None else InMemoryStorage()
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task with auto-generated ID.
        
        Args:
            title: Task title (required, cannot be empty)
            description: Optional task description
            
        Returns:
            The newly created Task
            
        Raises:
            ValueError: If title is empty or whitespace
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._storage.save(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> list[Task]:
        """Get all tasks, sorted by ID.
        
        Returns:
            List of all tasks, empty list if none exist
        """
        return self._storage.get_all()
    
    def get_task(self, task_id: int) -> Task | None:
        """Get a specific task by ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task if found, None otherwise
        """
        return self._storage.get_by_id(task_id)
    
    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None
    ) -> bool:
        """Update a task's title and/or description.
        
        Args:
            task_id: ID of the task to update
            title: New title (None to keep existing)
            description: New description (None to keep existing)
            
        Returns:
            True if task found and updated, False otherwise
            
        Note:
            Creates a new Task instance with updated values since Task is immutable-ish.
        """
        existing = self._storage.get_by_id(task_id)
        if existing is None:
            return False
        
        # Use existing values if not provided
        new_title = title if title is not None else existing.title
        new_description = description if description is not None else existing.description
        
        # Create updated task (preserving id and is_complete)
        updated_task = Task(
            id=existing.id,
            title=new_title,
            description=new_description,
            is_complete=existing.is_complete
        )
        self._storage.save(updated_task)
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if task found and deleted, False otherwise
        """
        return self._storage.delete(task_id)
    
    def toggle_complete(self, task_id: int) -> bool:
        """Toggle a task's completion status.
        
        Args:
            task_id: ID of the task to toggle
            
        Returns:
            True if task found and toggled, False otherwise
        """
        existing = self._storage.get_by_id(task_id)
        if existing is None:
            return False
        
        # Create task with toggled status
        toggled_task = Task(
            id=existing.id,
            title=existing.title,
            description=existing.description,
            is_complete=not existing.is_complete
        )
        self._storage.save(toggled_task)
        return True
    
    def get_task_count(self) -> int:
        """Get the total number of tasks.
        
        Returns:
            Count of all tasks
        """
        return len(self._storage.get_all())
    
    def get_completed_count(self) -> int:
        """Get the number of completed tasks.
        
        Returns:
            Count of completed tasks
        """
        return sum(1 for task in self._storage.get_all() if task.is_complete)
