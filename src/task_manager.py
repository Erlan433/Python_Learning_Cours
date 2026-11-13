"""Application facade connecting model, storage and interface."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path

try:
    from .interface_TM import Interface
    from .storage_manager import StorageManager
    from .task import Task
except ImportError:  # Support ``python src/main.py``.
    from interface_TM import Interface
    from storage_manager import StorageManager
    from task import Task


class TaskManager:
    """Coordinate all user actions without creating Tkinter widgets."""

    def __init__(self, root: tk.Tk, storage_path: str | Path | None = None) -> None:
        path = Path(storage_path) if storage_path else Path(__file__).with_name("saves.json")
        self.storage = StorageManager(path)
        self.interface = Interface(root)
        self.tasks: list[Task] = []
        self.interface.build(
            on_create=self.create_task,
            on_edit=self.edit_task,
            on_delete=self.delete_task,
            on_toggle=self.toggle_status,
            on_select=self.load_selected_task,
        )
        self.refresh()

    def create_task(self) -> None:
        data = self.interface.get_input()
        if not self._validate(data):
            return

        self.storage.add(
            Task(
                title=data["title"],
                description=data["description"],
                author=data["author"] or "—",
            )
        )
        self.interface.clear_input()
        self.refresh()

    def edit_task(self) -> None:
        selected = self._selected_task()
        if selected is None:
            return

        data = self.interface.get_input()
        if not self._validate(data, ignored_id=selected.id):
            return

        updated = Task(
            id=selected.id,
            title=data["title"],
            description=data["description"],
            author=data["author"] or "—",
            status=selected.status,
            created_at=selected.created_at,
        )
        self.storage.update(selected.id, updated)
        self.interface.clear_input()
        self.refresh()

    def delete_task(self) -> None:
        selected = self._selected_task()
        if selected is None:
            return
        if not self.interface.ask_confirm("Удаление", f"Удалить задачу «{selected.title}»?"):
            return
        self.storage.delete(selected.id)
        self.interface.clear_input()
        self.refresh()

    def toggle_status(self) -> None:
        selected = self._selected_task()
        if selected is None:
            return
        selected.status = not selected.status
        self.storage.update(selected.id, selected)
        self.refresh()

    def toggle_done(self) -> None:
        """Compatibility name for the task specification."""
        self.toggle_status()

    def load_selected_task(self) -> None:
        index = self.interface.get_selected_index()
        if index is None or index >= len(self.tasks):
            return
        task = self.tasks[index]
        self.interface.set_input(
            {
                "title": task.title,
                "description": task.description,
                "author": "" if task.author == "—" else task.author,
            }
        )

    def refresh(self) -> None:
        self.tasks = self.storage.load()
        self.interface.show_tasks(self.tasks)

    def run(self) -> None:
        self.interface.run()

    def _selected_task(self) -> Task | None:
        index = self.interface.get_selected_index()
        if index is None or index >= len(self.tasks):
            self.interface.show_warning("Выбор задачи", "Сначала выберите задачу в списке.")
            return None
        return self.tasks[index]

    def _validate(self, data: dict[str, str], ignored_id: int | None = None) -> bool:
        if not data["title"]:
            self.interface.show_warning("Проверка данных", "Название задачи не может быть пустым.")
            return False
        if any(
            task.title.casefold() == data["title"].casefold() and task.id != ignored_id
            for task in self.tasks
        ):
            self.interface.show_warning("Проверка данных", "Задача с таким названием уже существует.")
            return False
        return True
