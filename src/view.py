"""Функции отображения для консольной версии приложения."""


def show_collection(task_list):
    if not task_list:
        print("Список задач пуст.")
        return

    for number, task in enumerate(task_list, start=1):
        print(f"{number}. {task}")


def show_message(message="", mess_action=""):
    if message and mess_action:
        print(f"Задача '{message}' {mess_action}.")
    elif message:
        print(message)
