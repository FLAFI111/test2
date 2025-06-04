import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

TASKS_FILE = Path('tasks.json')

@dataclass
class Task:
    description: str
    done: bool = False

@dataclass
class TodoList:
    tasks: List[Task] = field(default_factory=list)
    file_path: Path = TASKS_FILE

    def load(self) -> None:
        if self.file_path.exists():
            data = json.loads(self.file_path.read_text())
            self.tasks = [Task(**item) for item in data]

    def save(self) -> None:
        data = [task.__dict__ for task in self.tasks]
        self.file_path.write_text(json.dumps(data, indent=2))

    def add(self, description: str) -> None:
        self.tasks.append(Task(description))
        self.save()

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def complete(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            self.save()
        else:
            raise IndexError('task index out of range')

    def remove(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()
        else:
            raise IndexError('task index out of range')
