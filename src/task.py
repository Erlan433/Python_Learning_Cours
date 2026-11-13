"""Domain model for a task."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Task:
    """A single task that can be serialized to JSON."""

    title: str
    description: str = ""
    status: bool = False
    author: str = "—"
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )
    id: int | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible representation of the task."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        """Create a task from data read from JSON."""
        if not isinstance(data, dict):
            raise TypeError("Task data must be a dictionary")

        title = str(data.get("title", "")).strip()
        if not title:
            raise ValueError("Task title cannot be empty")

        raw_id = data.get("id")
        task_id = int(raw_id) if raw_id is not None else None
        author = str(data.get("author", "—")).strip() or "—"

        return cls(
            title=title,
            description=str(data.get("description", "")).strip(),
            status=bool(data.get("status", False)),
            author=author,
            created_at=str(data.get("created_at") or datetime.now().isoformat(timespec="seconds")),
            id=task_id,
        )
