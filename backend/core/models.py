import uuid
from datetime import datetime

class Task:
    def __init__(self, title:str, description:str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.status = "pending"

    def mark_completed(self):
        self.status = "completed"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }