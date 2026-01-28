from .models import Task
from .storage import load_tasks, save_tasks, find_task
from .decorators import log_execution

@log_execution
def create_task(title: str, description: str):
    tasks = load_tasks()
    task = Task(title, description)
    tasks.append(task.to_dict())
    save_tasks(tasks)
    return task

@log_execution
def complete_task(task_id: str):
    tasks = load_tasks()
    task = find_task(task_id, tasks)
    task["status"] = "completed"
    save_tasks(tasks)
    return task