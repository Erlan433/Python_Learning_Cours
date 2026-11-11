def show_tasks(task_listbox, tasks):
    task_listbox.show_tasks(tasks)


def show_collection(tasks):
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def show_message(message="", mess_action=""):
    print(f"{message} {mess_action}".strip())
