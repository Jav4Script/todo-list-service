import pytest

from uuid import uuid4

from app.core.entities.task import Task


def test_create_task_success(create_task_use_case):
    task = create_task_use_case.execute("Test Task", "This is a test task.")

    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.id is not None


def test_create_task_failure(create_task_use_case):
    with pytest.raises(ValueError):
        create_task_use_case.execute("", "This task has no title.")


def test_get_task_success(create_task_use_case, get_task_use_case):
    task = create_task_use_case.execute("Test Task", "This is a test task.")
    retrieved_task = get_task_use_case.execute(task.id)

    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title
    assert retrieved_task.description == task.description


def test_get_task_failure(get_task_use_case):
    with pytest.raises(KeyError):
        get_task_use_case.execute(uuid4())


def test_list_tasks_success(create_task_use_case, list_tasks_use_case):
    create_task_use_case.execute("Test Task 1", "This is a test task 1.")
    create_task_use_case.execute("Test Task 2", "This is a test task 2.")
    tasks = list_tasks_use_case.execute()

    assert len(tasks) >= 2
    assert all(isinstance(task, Task) for task in tasks)


def test_update_task_success(
    create_task_use_case, update_task_use_case, get_task_use_case
):
    task = create_task_use_case.execute("Old Task", "Old description")
    task.title = "Updated Task"
    task.description = "Updated description"
    update_task_use_case.execute(task)
    updated_task = get_task_use_case.execute(task.id)

    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated description"


def test_update_task_failure(update_task_use_case):
    non_existent_task = Task("Non-existent Task", "This task does not exist.")
    non_existent_task.id = uuid4()

    with pytest.raises(KeyError):
        update_task_use_case.execute(non_existent_task)


def test_delete_task_success(
    create_task_use_case, delete_task_use_case, get_task_use_case
):
    task = create_task_use_case.execute(
        "Task to be deleted", "This task will be deleted"
    )
    delete_task_use_case.execute(task.id)

    with pytest.raises(KeyError):
        get_task_use_case.execute(task.id)


def test_delete_task_failure(delete_task_use_case):
    with pytest.raises(KeyError):
        delete_task_use_case.execute(uuid4())
