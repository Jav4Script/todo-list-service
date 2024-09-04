from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.task.entities.task import Task


# SOLID: Adheres to the Interface Segregation Principle by defining a specific interface for task repositories.
# Clean Code: Clear and descriptive interface name.
# DRY: Defines a common contract for all task repositories.
class ITaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> None:
        pass

    @abstractmethod
    def get(self, task_id: UUID) -> Task:
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[Task]:
        pass
