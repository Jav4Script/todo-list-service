from uuid import UUID

from app.shared.exceptions.custom_exceptions import NotFoundException
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on deleting a task.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the ITaskRepository interface.
class DeleteTaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, task_id: UUID) -> None:
        task = self.repository.get(task_id)

        if not task:
            raise NotFoundException(detail="Task not found.")

        self.repository.delete(task_id)
