from app.task.entities.task import Task
from app.task.repositories.task_repository import ITaskRepository


# SOLID: Adheres to the Single Responsibility Principle by focusing on deleting a task.
# Clean Code: Clear and descriptive class name.
# DRY: Reuses the ITaskRepository interface.
class CreateTaskUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, title: str, description: str = "") -> Task:
        task = Task(title, description)

        self.repository.add(task)

        return task
