"""Presentation layer for Task Manager."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from typing import Callable

try:
    from .components import AppButton, AppEntry, AppFrame, AppLabel, AppListbox, BACKGROUND
except ImportError:  # Support ``python src/main.py``.
    from components import AppButton, AppEntry, AppFrame, AppLabel, AppListbox, BACKGROUND


Callback = Callable[[], None]


class Interface:
    """A small facade over Tkinter used by ``TaskManager``."""

    def __init__(
        self,
        root: tk.Tk,
        title: str = "Task Manager",
        width: int = 680,
        height: int = 560,
    ) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(620, 500)
        self.root.configure(bg=BACKGROUND)

        icon_path = Path(__file__).resolve().parent.parent / "assets" / "image.ico"
        if icon_path.exists():
            try:
                self.root.iconbitmap(icon_path)
            except tk.TclError:
                pass

        self.title_entry: AppEntry | None = None
        self.description_entry: AppEntry | None = None
        self.author_entry: AppEntry | None = None
        self.task_listbox: AppListbox | None = None

    def run(self) -> None:
        self.root.mainloop()

    def quit(self) -> None:
        self.root.destroy()

    def clear(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

    def build(
        self,
        on_create: Callback,
        on_edit: Callback,
        on_delete: Callback,
        on_toggle: Callback,
        on_select: Callback,
    ) -> None:
        """Build the window and attach callbacks supplied by the manager."""
        self.clear()
        container = AppFrame(self.root, padx=24, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        AppLabel(
            container,
            "Менеджер задач",
            font=("Segoe UI", 20, "bold"),
        ).pack(anchor="w", pady=(0, 14))

        form = AppFrame(container)
        form.pack(fill=tk.X)
        form.columnconfigure(1, weight=1)

        AppLabel(form, "Название:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=4)
        self.title_entry = AppEntry(form)
        self.title_entry.grid(row=0, column=1, sticky="ew", pady=4)

        AppLabel(form, "Описание:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=4)
        self.description_entry = AppEntry(form)
        self.description_entry.grid(row=1, column=1, sticky="ew", pady=4)

        AppLabel(form, "Автор:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=4)
        self.author_entry = AppEntry(form)
        self.author_entry.grid(row=2, column=1, sticky="ew", pady=4)

        actions = AppFrame(container)
        actions.pack(fill=tk.X, pady=12)
        AppButton(actions, "Добавить", on_create).pack(side=tk.LEFT, padx=(0, 6))
        AppButton(actions, "Сохранить", on_edit).pack(side=tk.LEFT, padx=6)
        AppButton(actions, "Выполнено", on_toggle).pack(side=tk.LEFT, padx=6)
        AppButton(actions, "Удалить", on_delete, bg="#dc2626", activebackground="#b91c1c").pack(
            side=tk.LEFT, padx=6
        )
        self.task_listbox = AppListbox(container, height=14)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        self.task_listbox.bind("<<ListboxSelect>>", lambda _event: on_select())

    def get_input(self) -> dict[str, str]:
        return {
            "title": self.title_entry.get().strip() if self.title_entry else "",
            "description": self.description_entry.get().strip() if self.description_entry else "",
            "author": self.author_entry.get().strip() if self.author_entry else "",
        }

    def set_input(self, data: dict[str, str]) -> None:
        entries = (
            (self.title_entry, data.get("title", "")),
            (self.description_entry, data.get("description", "")),
            (self.author_entry, data.get("author", "")),
        )
        for entry, value in entries:
            if entry is not None:
                entry.delete(0, tk.END)
                entry.insert(0, value)

    def clear_input(self) -> None:
        self.set_input({})

    def show_tasks(self, tasks: list) -> None:
        if self.task_listbox is None:
            return
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            mark = "✓" if task.status else "○"
            author = f" — {task.author}" if task.author and task.author != "—" else ""
            created_at = task.created_at.replace("T", " ")
            self.task_listbox.insert(
                tk.END,
                f"{mark}  {task.title}{author}  |  Создано: {created_at}",
            )

    def show_message(self, title: str, text: str) -> None:
        messagebox.showinfo(title, text, parent=self.root)

    def show_warning(self, title: str, text: str) -> None:
        messagebox.showwarning(title, text, parent=self.root)

    def ask_confirm(self, title: str, text: str) -> bool:
        return messagebox.askyesno(title, text, parent=self.root)

    def get_selected_index(self) -> int | None:
        if self.task_listbox is None:
            return None
        selection = self.task_listbox.curselection()
        return int(selection[0]) if selection else None
