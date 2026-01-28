from pathlib import Path
from core.services import create_task, complete_task

task = create_task("Test Task", "This is a test task.")
print("Created Task:", task)

completed = complete_task(task.id)
print("Completed Task:", completed)