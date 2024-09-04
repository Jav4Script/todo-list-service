import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


def get_postgres_uri():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    dbname = os.getenv("POSTGRES_DB")

    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"


def init_database():
    DATABASE_URL = get_postgres_uri()
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    return SessionLocal


def get_database():
    SessionLocal = init_database()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Clean Code: Configuration and initialization logic is encapsulated in functions.
# DRY: Reuses environment variables for configuration.
# KISS: Simple functions to handle database configuration and initialization.
# SOLID: Adheres to the Dependency Inversion Principle by using dependency injection for the database session.
# Good practice: Using context management (try/finally) to ensure the database session is properly closed.
