"""Entry point for Task Manager v0.2.0."""

import tkinter as tk

try:
    from .task_manager import TaskManager
except ImportError:  # Support ``python src/main.py``.
    from task_manager import TaskManager


def main() -> None:
    root = tk.Tk()
    app = TaskManager(root)
    app.run()


if __name__ == "__main__":
    main()
