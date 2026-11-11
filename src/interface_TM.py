import tkinter as tk
from pathlib import Path

from AppButton import AppButton
from AppLabel import AppLabel
from AppListbox import AppListbox
from config import NAME_FILE_SAVES
from storage import load_collection, save_collection
from view import show_tasks


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Task Manager")
        self.root.iconbitmap(Path(__file__).resolve().parent.parent / "assets" / "image.ico")
        self.tasks = load_collection([], NAME_FILE_SAVES)

        AppLabel(self.root, "Мои задачи").pack(pady=10)
        self.task_input = tk.Entry(self.root, width=32)
        self.task_input.pack(pady=5)
        AppButton(self.root, "Добавить", self.add_task).pack(pady=5)

        self.task_listbox = AppListbox(self.root, width=45, height=12)
        self.task_listbox.pack(pady=10)
        AppButton(self.root, "Обновить", self.show_tasks).pack()
        self.show_tasks()

    def add_task(self):
        task = self.task_input.get().strip()
        if task and task not in self.tasks:
            self.tasks.append(task)
            save_collection(self.tasks, NAME_FILE_SAVES)
            self.task_input.delete(0, tk.END)
            self.show_tasks()

    def show_tasks(self):
        show_tasks(self.task_listbox, self.tasks)
