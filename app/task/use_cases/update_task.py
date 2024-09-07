from app.shared.exceptions.custom_exceptions import NotFoundException
from app.task.entities.task import Task, TaskCreate
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on deleting a task.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the ITaskRepository interface.
class UpdateTaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, task_id, task_data: TaskCreate) -> Task:
        existing_task = self.repository.get(task_id=task_id)

        if not existing_task:
            raise NotFoundException(detail="Task not found.")

        task = Task(
            id=existing_task.id,
            title=task_data.title,
            description=task_data.description,
        )

        self.repository.update(task)

        return task
