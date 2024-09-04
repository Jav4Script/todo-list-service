from typing import List

from app.task.entities.task import Task
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on listing tasks.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the Task entity and ITaskRepository interface.
class ListTasksUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self) -> List[Task]:
        return self.repository.list()
