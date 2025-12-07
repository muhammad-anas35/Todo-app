"""Main entry point for the Todo Console Application.

Run with: uv run python -m src
Or after installation: todo
"""

import sys

from src.cli.menu import TodoMenu


def main() -> int:
    """Main entry point for the todo console application.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        menu = TodoMenu()
        menu.run()
        return 0
    
    except KeyboardInterrupt:
        print("\n\n  👋 Interrupted. Goodbye!\n")
        return 0
    
    except Exception as e:
        print(f"\n  ❌ An unexpected error occurred: {e}\n", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
