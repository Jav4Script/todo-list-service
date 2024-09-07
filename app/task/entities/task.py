from dataclasses import dataclass, field
from datetime import datetime, timezone
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional


@dataclass
class Task:
    title: str
    description: Optional[str] = field(default=None)
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def update(self, title: str, description: Optional[str] = None):
        self.title = title
        self.description = description if description is not None else self.description
        self.updated_at = datetime.now(timezone.utc)


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
