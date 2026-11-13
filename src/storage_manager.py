"""JSON persistence for tasks."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from .task import Task
except ImportError:  # Support ``python src/main.py``.
    from task import Task


class StorageManager:
    """Load and mutate a collection of tasks stored in a JSON file."""

    def __init__(self, path: str | Path = "tasks.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.save([])

    def load(self) -> list[Task]:
        """Read all valid tasks; an absent or damaged file produces an empty list."""
        try:
            raw_data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return []

        if not isinstance(raw_data, list):
            return []

        tasks: list[Task] = []
        used_ids: set[int] = set()
        next_id = 1

        for item in raw_data:
            try:
                # Compatibility with versions 0.0.x, where a task was a string.
                task = Task(title=item) if isinstance(item, str) else Task.from_dict(item)
            except (TypeError, ValueError):
                continue

            if task.id is None or task.id in used_ids:
                while next_id in used_ids:
                    next_id += 1
                task.id = next_id

            used_ids.add(task.id)
            next_id = max(next_id, task.id + 1)
            tasks.append(task)

        return tasks

    def save(self, tasks: list[Task]) -> None:
        """Write the complete task collection using UTF-8 JSON."""
        payload = [task.to_dict() for task in tasks]
        self.path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, task: Task) -> None:
        tasks = self.load()
        task.id = max((item.id or 0 for item in tasks), default=0) + 1
        tasks.append(task)
        self.save(tasks)

    def update(self, task_id: int, task: Task) -> None:
        tasks = self.load()
        for index, current in enumerate(tasks):
            if current.id == task_id:
                task.id = task_id
                tasks[index] = task
                self.save(tasks)
                return
        raise KeyError(f"Task with id={task_id} was not found")

    def delete(self, task_id: int) -> None:
        tasks = self.load()
        filtered = [task for task in tasks if task.id != task_id]
        if len(filtered) == len(tasks):
            raise KeyError(f"Task with id={task_id} was not found")
        self.save(filtered)
