import pytest

from uuid import uuid4
from unittest.mock import MagicMock

from app.task.entities.task import Task, TaskCreate
from app.shared.exceptions.custom_exceptions import NotFoundException
from app.task.use_cases.create_task import CreateTaskUseCase
from app.task.use_cases.delete_task import DeleteTaskUseCase
from app.task.use_cases.get_task import GetTaskUseCase
from app.task.use_cases.list_tasks import ListTasksUseCase
from app.task.use_cases.update_task import UpdateTaskUseCase


def test_create_task_success(
    create_task_use_case: CreateTaskUseCase, tasks: list[Task]
):
    task_data = TaskCreate(title=tasks[0].title, description=tasks[0].description)

    created_task = create_task_use_case.execute(task_data)

    assert created_task.title == task_data.title
    assert created_task.description == task_data.description
    assert created_task.id is not None


def test_create_task_failure(create_task_use_case: CreateTaskUseCase):
    create_task_use_case.execute = MagicMock(side_effect=ValueError)

    with pytest.raises(ValueError):
        create_task_use_case.execute(
            TaskCreate(title="", description="This task has no title.")
        )


def test_get_task_success(get_task_use_case: GetTaskUseCase, tasks: list[Task]):
    task = tasks[0]
    get_task_use_case.execute = MagicMock(return_value=task)

    retrieved_task = get_task_use_case.execute(task.id)

    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title
    assert retrieved_task.description == task.description


def test_get_task_failure(get_task_use_case: GetTaskUseCase):
    get_task_use_case.execute = MagicMock(side_effect=NotFoundException)

    with pytest.raises(NotFoundException):
        get_task_use_case.execute(uuid4())


def test_list_tasks_success(list_tasks_use_case: ListTasksUseCase, tasks: list[Task]):
    task1 = tasks[0]
    task2 = tasks[1]

    list_tasks_use_case.execute = MagicMock(return_value=[task1, task2])

    listed_tasks = list_tasks_use_case.execute()

    assert len(listed_tasks) >= 2
    assert all(isinstance(task, Task) for task in listed_tasks)


def test_update_task_success(
    update_task_use_case: UpdateTaskUseCase, tasks: list[Task]
):
    task = tasks[0]
    task_data = TaskCreate(title=task.title, description=task.description)

    update_task_use_case.execute = MagicMock(return_value=task)

    updated_task = update_task_use_case.execute(task.id, task_data)

    assert updated_task.id == task.id
    assert updated_task.title == task_data.title
    assert updated_task.description == task_data.description


def test_update_task_failure(update_task_use_case: UpdateTaskUseCase):
    non_existent_task_id = uuid4()
    task_data = TaskCreate(
        title="Non-existent Task", description="This task does not exist."
    )

    update_task_use_case.execute = MagicMock(side_effect=NotFoundException)

    with pytest.raises(NotFoundException):
        update_task_use_case.execute(non_existent_task_id, task_data)


def test_delete_task_success(
    delete_task_use_case: DeleteTaskUseCase,
    get_task_use_case: GetTaskUseCase,
    tasks: list[Task],
):
    task = tasks[0]
    delete_task_use_case.execute = MagicMock()
    get_task_use_case.execute = MagicMock(side_effect=NotFoundException)

    delete_task_use_case.execute(task.id)

    with pytest.raises(NotFoundException):
        get_task_use_case.execute(task.id)


def test_delete_task_failure(delete_task_use_case: DeleteTaskUseCase):
    delete_task_use_case.execute = MagicMock(side_effect=NotFoundException)

    with pytest.raises(NotFoundException):
        delete_task_use_case.execute(uuid4())
