"""Tests for the Task model."""

import pytest

from src.models.task import Task


class TestTaskCreation:
    """Tests for Task instantiation and validation."""
    
    def test_create_task_with_all_fields(self) -> None:
        """Task can be created with all fields specified."""
        task = Task(id=1, title="Test Task", description="Test Description", is_complete=True)
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.is_complete is True
    
    def test_create_task_with_defaults(self) -> None:
        """Task uses correct defaults for optional fields."""
        task = Task(id=1, title="Test Task")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.is_complete is False
    
    def test_title_is_stripped(self) -> None:
        """Title whitespace is trimmed during creation."""
        task = Task(id=1, title="  Padded Title  ")
        
        assert task.title == "Padded Title"
    
    def test_description_is_stripped(self) -> None:
        """Description whitespace is trimmed during creation."""
        task = Task(id=1, title="Test", description="  Padded Desc  ")
        
        assert task.description == "Padded Desc"
    
    def test_empty_title_raises_error(self) -> None:
        """Empty title raises ValueError."""
        with pytest.raises(ValueError, match="title cannot be empty"):
            Task(id=1, title="")
    
    def test_whitespace_only_title_raises_error(self) -> None:
        """Whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="title cannot be empty"):
            Task(id=1, title="   ")


class TestTaskStatusIcon:
    """Tests for status icon display."""
    
    def test_incomplete_task_shows_circle(self) -> None:
        """Incomplete task shows ○ icon."""
        task = Task(id=1, title="Test", is_complete=False)
        
        assert task.status_icon == "○"
    
    def test_complete_task_shows_checkmark(self) -> None:
        """Complete task shows ✓ icon."""
        task = Task(id=1, title="Test", is_complete=True)
        
        assert task.status_icon == "✓"


class TestTaskDisplayString:
    """Tests for task display formatting."""
    
    def test_display_without_description(self) -> None:
        """Display string without description is formatted correctly."""
        task = Task(id=1, title="Buy groceries")
        
        result = task.to_display_string()
        
        assert result == "○ [1] Buy groceries"
    
    def test_display_with_description(self) -> None:
        """Display string with description includes it."""
        task = Task(id=1, title="Buy groceries", description="Milk, eggs")
        
        result = task.to_display_string()
        
        assert result == "○ [1] Buy groceries - Milk, eggs"
    
    def test_display_complete_task(self) -> None:
        """Complete task shows checkmark in display."""
        task = Task(id=1, title="Done task", is_complete=True)
        
        result = task.to_display_string()
        
        assert result == "✓ [1] Done task"
    
    def test_display_without_description_flag(self) -> None:
        """Can hide description in display string."""
        task = Task(id=1, title="Test", description="Hidden")
        
        result = task.to_display_string(show_description=False)
        
        assert result == "○ [1] Test"
        assert "Hidden" not in result
