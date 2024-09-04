import uuid

from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime

from app.task.infrastructure.config.database import Base


# Good practice: Using SQLAlchemy ORM for database modeling, which abstracts SQL queries and provides a clean interface.
# Clean Code: Clear and descriptive naming for columns and class attributes.
# DRY: Default values and automatic timestamping reduce repetitive code.
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, description=""):
        self.title = title
        self.description = description
