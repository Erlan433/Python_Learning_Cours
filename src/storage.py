""" =========================================================
        Модуль для сохранения и загрузки задач в файл
    =========================================================
"""

import json


def load_collection(task_list, file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            saved_tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        saved_tasks = []

    if isinstance(saved_tasks, list):
        task_list.extend(saved_tasks)

    return task_list


"""сохранение"""


def save_collection(task_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(task_list, file, ensure_ascii=False, indent=2)
