from fastapi import APIRouter, FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.task.use_cases.create_task import CreateTaskUseCase
from app.task.use_cases.delete_task import DeleteTaskUseCase
from app.task.use_cases.get_task import GetTaskUseCase
from app.task.use_cases.list_tasks import ListTasksUseCase
from app.task.use_cases.update_task import UpdateTaskUseCase
from app.task.infrastructure.database.task_repository import SQLAlchemyTaskRepository
from app.task.infrastructure.config.database import get_database

router = APIRouter()


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201,
    summary="Create a new task",
    description="Create a new task with a title and optional description.",
)
def create_task_controller(data: TaskCreate, database: Session = Depends(get_database)):
    use_case = CreateTaskUseCase(SQLAlchemyTaskRepository(database))
    task = use_case.execute(data.title, data.description)

    return {"id": task.id, "title": task.title, "description": task.description}


@router.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete a task",
    description="Delete a task by its ID.",
)
def delete_task_controller(task_id: str, database: Session = Depends(get_database)):
    use_case = DeleteTaskUseCase(SQLAlchemyTaskRepository(database))
    use_case.execute(task_id)

    return


@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=200,
    summary="Get a task",
    description="Get a task by its ID.",
)
def get_task_controller(task_id: str, database: Session = Depends(get_database)):
    use_case = GetTaskUseCase(SQLAlchemyTaskRepository(database))
    task = use_case.execute(task_id)

    return {"id": task.id, "title": task.title, "description": task.description}


@router.get(
    "/tasks",
    response_model=List[TaskResponse],
    status_code=200,
    summary="List all tasks",
    description="List all tasks.",
)
def list_tasks_controller(database: Session = Depends(get_database)):
    use_case = ListTasksUseCase(SQLAlchemyTaskRepository(database))
    tasks = use_case.execute()

    return [
        {"id": task.id, "title": task.title, "description": task.description}
        for task in tasks
    ]


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=200,
    summary="Update a task",
    description="Update a task by its ID.",
)
def update_task_controller(
    task_id: str, data: TaskCreate, database: Session = Depends(get_database)
):
    use_case = UpdateTaskUseCase(SQLAlchemyTaskRepository(database))
    task = use_case.execute(task_id, data.title, data.description)

    return {"id": task.id, "title": task.title, "description": task.description}


def register_routes(app: FastAPI):
    app.include_router(router, prefix="/api")
