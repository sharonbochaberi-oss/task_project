from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks):

    title = input("Enter task title: ")
    if not validate_task_title(title):
        return

    description = input("Enter task description: ")
    if not validate_task_description(description):
        return

    due_date = input("Enter due date (YYYY-MM-DD): ")
    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully.")


def mark_task_as_complete(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i}: {task['title']}")

    index = int(input("Enter task number to mark as complete: "))

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["completed"] = True

    print("Task marked as complete.")


def view_pending_tasks(tasks):

    pending_found = False

    for task in tasks:
        if not task["completed"]:
            print(task["title"], "-", task["due_date"])
            pending_found = True

    if not pending_found:
        print("No pending tasks.")


def calculate_progress(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    completed = sum(1 for task in tasks if task["completed"])
    total = len(tasks)

    print(f"Progress: {completed}/{total} tasks completed.")