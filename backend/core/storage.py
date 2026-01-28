import json
from pathlib import Path
from .exceptions import TaskNotFoundError

DATA_FILE = Path("tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def find_task(task_id, tasks):
    for task in tasks:
        if task["id"] == task_id:
            return task
        else:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")