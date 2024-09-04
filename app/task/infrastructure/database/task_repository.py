from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from app.task.entities.task import Task
from app.task.repositories.task_repository import ITaskRepository
from app.task.infrastructure.orm.task_model import TaskModel


# SOLID: Adheres to the Dependency Inversion Principle by depending on abstractions (ITaskRepository).
# SOLID: Adheres to the Single Responsibility Principle by focusing on listing tasks.
# Clean Code: Separation of concerns by isolating database operations in a repository class.
# DRY: Reuses the TaskModel for database operations.
class SQLAlchemyTaskRepository(ITaskRepository):
    def __init__(self, database: Session):
        self.database = database

    def add(self, task: Task) -> None:
        task_model = TaskModel(title=task.title, description=task.description)
        self.database.add(task_model)
        self.database.commit()

    def get(self, task_id: UUID) -> Task:
        task_model = self.database.query(TaskModel).filter_by(id=str(task_id)).first()
        if task_model:
            return Task(
                id=task_model.id,
                title=task_model.title,
                description=task_model.description,
                created_at=task_model.created_at,
                updated_at=task_model.updated_at,
            )
        return None

    def update(self, task: Task) -> None:
        task_model = self.database.query(TaskModel).filter_by(id=str(task.id)).first()
        if task_model:
            task_model.title = task.title
            task_model.description = task.description
            self.database.commit()

    def delete(self, task_id: UUID) -> None:
        task_model = self.database.query(TaskModel).filter_by(id=str(task_id)).first()
        if task_model:
            self.database.delete(task_model)
            self.database.commit()

    def list(self) -> List[Task]:
        task_models = self.database.query(TaskModel).all()
        return [
            Task(
                id=task.id,
                title=task.title,
                description=task.description,
                created_at=task.created_at,
                updated_at=task.updated_at,
            )
            for task in task_models
        ]
