
import json
from pathlib import Path


class TaskStorage:
    """Save and load tasks using a JSON file."""

    def __init__(self, file_path="tasks.json"):
        self.file_path = Path(file_path)

    def save(self, tasks: list) -> None:
        self.file_path.write_text(
            json.dumps(tasks, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self) -> list:
        if not self.file_path.exists():
            return []

        data = json.loads(self.file_path.read_text(encoding="utf-8"))

        if not isinstance(data, list):
            raise ValueError("Format penyimpanan tugas tidak valid.")

        return data
from .models import Task

class TaskStorage:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title):
        task = Task(id=self._next_id, title=title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def all(self):
        return list(self._tasks.values())

    def get(self, task_id):
        return self._tasks.get(task_id)

    def complete(self, task_id):
        task = self._tasks.get(task_id)
        if task:
            task.done = True
        return task

    def delete(self, task_id):
        return self._tasks.pop(task_id, None) is not None