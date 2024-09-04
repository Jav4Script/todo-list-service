import pytest

from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app
from app.task.infrastructure.database.task_repository import SQLAlchemyTaskRepository
from app.core.use_cases.create_task import CreateTaskUseCase
from app.core.use_cases.delete_task import DeleteTaskUseCase
from app.core.use_cases.get_task import GetTaskUseCase
from app.core.use_cases.list_tasks import ListTasksUseCase
from app.core.use_cases.update_task import UpdateTaskUseCase


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def repository():
    return MagicMock()


@pytest.fixture(scope="module")
def create_task_use_case(repository):
    return CreateTaskUseCase(repository)


@pytest.fixture(scope="module")
def delete_task_use_case(repository):
    return DeleteTaskUseCase(repository)


@pytest.fixture(scope="module")
def get_task_use_case(repository):
    return GetTaskUseCase(repository)


@pytest.fixture(scope="module")
def list_tasks_use_case(repository):
    return ListTasksUseCase(repository)


@pytest.fixture(scope="module")
def update_task_use_case(repository):
    return UpdateTaskUseCase(repository)
