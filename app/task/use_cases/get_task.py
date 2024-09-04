from uuid import UUID

from app.shared.exceptions.custom_exceptions import NotFoundException
from app.task.entities.task import Task
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on retrieving a task.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the Task entity and ITaskRepository interface.
class GetTaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, task_id: UUID) -> Task:
        task = self.repository.get(task_id)

        if not task:
            raise NotFoundException(detail="Task not found.")

        return task
