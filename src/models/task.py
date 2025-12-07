"""Task model - Represents a todo item with id, title, description, and status.

This module provides the core data structure for the todo application.
Uses Python 3.10+ dataclass features for memory efficiency and type safety.
"""

from dataclasses import dataclass, field


@dataclass(slots=True, kw_only=True)
class Task:
    """A todo task with unique ID, title, description, and completion status.
    
    Attributes:
        id: Unique identifier for the task (auto-assigned by TaskManager)
        title: The task title (required, 1-100 characters)
        description: Optional description with additional details
        is_complete: Whether the task has been completed (default: False)
    
    Example:
        >>> task = Task(id=1, title="Buy groceries", description="Milk, eggs")
        >>> task.is_complete
        False
        >>> task.title
        'Buy groceries'
    """
    
    id: int
    title: str
    description: str = field(default="")
    is_complete: bool = field(default=False)
    
    def __post_init__(self) -> None:
        """Validate task data after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        
        # Normalize title (strip whitespace)
        object.__setattr__(self, "title", self.title.strip())
        
        # Normalize description
        if self.description:
            object.__setattr__(self, "description", self.description.strip())
    
    @property
    def status_icon(self) -> str:
        """Return visual status indicator for display.
        
        Returns:
            '✓' if complete, '○' if incomplete
        """
        return "✓" if self.is_complete else "○"
    
    def to_display_string(self, show_description: bool = True) -> str:
        """Format task for console display.
        
        Args:
            show_description: Whether to include description in output
            
        Returns:
            Formatted string like "○ [1] Buy groceries - Milk, eggs"
        """
        base = f"{self.status_icon} [{self.id}] {self.title}"
        if show_description and self.description:
            return f"{base} - {self.description}"
        return base
