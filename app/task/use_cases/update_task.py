from app.shared.exceptions.custom_exceptions import NotFoundException
from app.task.entities.task import Task
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on deleting a task.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the ITaskRepository interface.
class UpdateTaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, task: Task) -> None:
        existing_task = self.repository.get(task.id)

        if not existing_task:
            raise NotFoundException(detail="Task not found.")

        self.repository.update(task)
