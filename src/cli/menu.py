"""CLI Menu - Interactive console interface for the todo application.

This module provides the user interface layer with reusable input helpers.
Follows the separation of concerns principle - UI logic separate from business logic.
"""

import os
import sys
from typing import Callable

from src.models.task import Task
from src.services.task_manager import TaskManager


# =============================================================================
# Reusable Input Helpers
# =============================================================================

def clear_screen() -> None:
    """Clear the console screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title: str, width: int = 50) -> None:
    """Print a formatted header with borders.
    
    Args:
        title: The header text
        width: Total width of the header box
    """
    print("\n" + "=" * width)
    print(f" {title.center(width - 2)} ")
    print("=" * width)


def print_divider(char: str = "-", width: int = 50) -> None:
    """Print a divider line."""
    print(char * width)


def get_input(prompt: str, required: bool = True, validator: Callable[[str], bool] | None = None) -> str:
    """Get validated input from user.
    
    Args:
        prompt: The prompt to display
        required: Whether input is required (cannot be empty)
        validator: Optional function to validate input
        
    Returns:
        The validated input string
    """
    while True:
        value = input(prompt).strip()
        
        if required and not value:
            print("  ⚠ This field is required. Please try again.")
            continue
        
        if validator and value and not validator(value):
            print("  ⚠ Invalid input. Please try again.")
            continue
        
        return value


def get_int_input(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """Get a validated integer input from user.
    
    Args:
        prompt: The prompt to display
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)
        
    Returns:
        The validated integer
    """
    while True:
        value = input(prompt).strip()
        
        try:
            num = int(value)
            
            if min_val is not None and num < min_val:
                print(f"  ⚠ Value must be at least {min_val}.")
                continue
            
            if max_val is not None and num > max_val:
                print(f"  ⚠ Value must be at most {max_val}.")
                continue
            
            return num
            
        except ValueError:
            print("  ⚠ Please enter a valid number.")


def confirm(prompt: str, default: bool = False) -> bool:
    """Get a yes/no confirmation from user.
    
    Args:
        prompt: The question to ask
        default: Default value if user just presses Enter
        
    Returns:
        True for yes, False for no
    """
    suffix = " [Y/n]: " if default else " [y/N]: "
    response = input(prompt + suffix).strip().lower()
    
    if not response:
        return default
    
    return response in ("y", "yes", "1", "true")


def pause(message: str = "Press Enter to continue...") -> None:
    """Pause execution until user presses Enter."""
    input(f"\n{message}")


# =============================================================================
# Menu Display Components
# =============================================================================

def display_menu_options(options: list[tuple[str, str]]) -> None:
    """Display numbered menu options.
    
    Args:
        options: List of (number, description) tuples
    """
    print()
    for num, desc in options:
        print(f"  [{num}] {desc}")
    print()


def display_task_list(tasks: list[Task], show_empty_message: bool = True) -> None:
    """Display a formatted list of tasks.
    
    Args:
        tasks: List of tasks to display
        show_empty_message: Whether to show message when no tasks
    """
    if not tasks:
        if show_empty_message:
            print("\n  📭 No tasks found.\n")
        return
    
    print()
    for task in tasks:
        print(f"  {task.to_display_string()}")
    print()


def display_task_stats(manager: TaskManager) -> None:
    """Display task statistics."""
    total = manager.get_task_count()
    completed = manager.get_completed_count()
    pending = total - completed
    
    print(f"\n  📊 Tasks: {total} total | ✓ {completed} done | ○ {pending} pending\n")


# =============================================================================
# TodoMenu Class
# =============================================================================

class TodoMenu:
    """Interactive CLI menu for managing todo tasks.
    
    Provides a numbered menu interface for all CRUD operations.
    Uses dependency injection for TaskManager to enable testing.
    
    Attributes:
        manager: The TaskManager instance to use
        
    Example:
        >>> menu = TodoMenu()
        >>> menu.run()  # Starts interactive loop
    """
    
    MENU_OPTIONS = [
        ("1", "Add Task"),
        ("2", "View All Tasks"),
        ("3", "Update Task"),
        ("4", "Delete Task"),
        ("5", "Mark Complete/Incomplete"),
        ("6", "Exit"),
    ]
    
    def __init__(self, manager: TaskManager | None = None) -> None:
        """Initialize menu with optional TaskManager.
        
        Args:
            manager: TaskManager instance (creates new one if None)
        """
        self.manager = manager if manager is not None else TaskManager()
        self._running = False
    
    def run(self) -> None:
        """Start the interactive menu loop."""
        self._running = True
        
        clear_screen()
        print_header("📝 TODO CONSOLE APP")
        print("\n  Welcome! Manage your tasks with ease.\n")
        pause()
        
        while self._running:
            self._show_main_menu()
    
    def stop(self) -> None:
        """Stop the menu loop."""
        self._running = False
    
    def _show_main_menu(self) -> None:
        """Display main menu and handle selection."""
        clear_screen()
        print_header("📝 TODO CONSOLE APP")
        display_task_stats(self.manager)
        print_divider()
        display_menu_options(self.MENU_OPTIONS)
        
        choice = get_input("Enter choice: ")
        
        actions: dict[str, Callable[[], None]] = {
            "1": self._add_task,
            "2": self._view_tasks,
            "3": self._update_task,
            "4": self._delete_task,
            "5": self._toggle_complete,
            "6": self._exit,
        }
        
        action = actions.get(choice)
        if action:
            action()
        else:
            print("  ⚠ Invalid choice. Please try again.")
            pause()
    
    def _add_task(self) -> None:
        """Handle adding a new task."""
        clear_screen()
        print_header("➕ ADD NEW TASK")
        
        title = get_input("  Title: ", required=True)
        description = get_input("  Description (optional): ", required=False)
        
        try:
            task = self.manager.add_task(title, description)
            print(f"\n  ✅ Task added successfully!")
            print(f"     {task.to_display_string()}")
        except ValueError as e:
            print(f"\n  ❌ Error: {e}")
        
        pause()
    
    def _view_tasks(self) -> None:
        """Handle viewing all tasks."""
        clear_screen()
        print_header("📋 ALL TASKS")
        
        tasks = self.manager.get_all_tasks()
        display_task_list(tasks)
        display_task_stats(self.manager)
        
        pause()
    
    def _update_task(self) -> None:
        """Handle updating an existing task."""
        clear_screen()
        print_header("✏️ UPDATE TASK")
        
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("\n  📭 No tasks to update.\n")
            pause()
            return
        
        display_task_list(tasks)
        print_divider()
        
        task_id = get_int_input("  Enter task ID to update: ", min_val=1)
        
        existing = self.manager.get_task(task_id)
        if not existing:
            print(f"\n  ❌ Task with ID {task_id} not found.")
            pause()
            return
        
        print(f"\n  Current: {existing.to_display_string()}")
        print("  (Press Enter to keep current value)\n")
        
        new_title = input(f"  New title [{existing.title}]: ").strip()
        new_description = input(f"  New description [{existing.description or '(none)'}]: ").strip()
        
        # Use None for unchanged values
        title = new_title if new_title else None
        description = new_description if new_description else None
        
        if title or description:
            self.manager.update_task(task_id, title=title, description=description)
            updated = self.manager.get_task(task_id)
            print(f"\n  ✅ Task updated!")
            print(f"     {updated.to_display_string() if updated else ''}")
        else:
            print("\n  ℹ️ No changes made.")
        
        pause()
    
    def _delete_task(self) -> None:
        """Handle deleting a task."""
        clear_screen()
        print_header("🗑️ DELETE TASK")
        
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("\n  📭 No tasks to delete.\n")
            pause()
            return
        
        display_task_list(tasks)
        print_divider()
        
        task_id = get_int_input("  Enter task ID to delete: ", min_val=1)
        
        existing = self.manager.get_task(task_id)
        if not existing:
            print(f"\n  ❌ Task with ID {task_id} not found.")
            pause()
            return
        
        print(f"\n  Task: {existing.to_display_string()}")
        
        if confirm("  Are you sure you want to delete this task?"):
            self.manager.delete_task(task_id)
            print("\n  ✅ Task deleted successfully!")
        else:
            print("\n  ℹ️ Deletion cancelled.")
        
        pause()
    
    def _toggle_complete(self) -> None:
        """Handle toggling task completion status."""
        clear_screen()
        print_header("✓ TOGGLE COMPLETE/INCOMPLETE")
        
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("\n  📭 No tasks to toggle.\n")
            pause()
            return
        
        display_task_list(tasks)
        print_divider()
        
        task_id = get_int_input("  Enter task ID to toggle: ", min_val=1)
        
        existing = self.manager.get_task(task_id)
        if not existing:
            print(f"\n  ❌ Task with ID {task_id} not found.")
            pause()
            return
        
        old_status = "complete" if existing.is_complete else "incomplete"
        self.manager.toggle_complete(task_id)
        updated = self.manager.get_task(task_id)
        new_status = "complete" if updated and updated.is_complete else "incomplete"
        
        print(f"\n  ✅ Task marked as {new_status}!")
        if updated:
            print(f"     {updated.to_display_string()}")
        
        pause()
    
    def _exit(self) -> None:
        """Handle exit confirmation."""
        clear_screen()
        print_header("👋 EXIT")
        
        if confirm("\n  Are you sure you want to exit?"):
            print("\n  Thank you for using Todo Console App!")
            print("  Goodbye! 👋\n")
            self.stop()
        else:
            print("\n  ℹ️ Returning to main menu...")
            pause()
