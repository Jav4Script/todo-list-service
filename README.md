# TODO-LIST Backend

- [TODO-LIST Backend](#todo-list-backend)
  - [Technology](#technology)
  - [📜 Description](#-description)
  - [🏗️ Project Structure](#️-project-structure)
  - [🚀 Project Setup](#-project-setup)
    - [1. Prerequisites](#1-prerequisites)
    - [2. Clone the Repository](#2-clone-the-repository)
    - [3. Configure the Database with Docker](#3-configure-the-database-with-docker)
    - [4. Configure the Python Environment](#4-configure-the-python-environment)
    - [5. Configure the Database](#5-configure-the-database)
    - [6. Run the Application](#6-run-the-application)
    - [7. Run the Tests](#7-run-the-tests)
  - [📚 API Documentation](#-api-documentation)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🧑‍💻 Contributing](#-contributing)
  - [📄 License](#-license)

## Technology

![Python](https://img.shields.io/badge/Python-3.8-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)

## 📜 Description

This project is a simple TODO-LIST system, developed with **Python** and **FastAPI**, using **PostgreSQL** as the database and following the **Clean Architecture** design pattern. The goal is to provide a robust, scalable, and easy-to-maintain RESTful API.

## 🏗️ Project Structure

- **app/shared**: Shared modules and utilities.
  - **exceptions**: Custom exceptions used across the application.
  - **infrastructure**: Shared infrastructure code.
- **app/task**: Task-related modules.
  - **entities**: Task domain entities.
  - **repositories**: Task repository interfaces.
  - **infrastructure**: Concrete implementations of task repositories.
  - **controllers**: Task-related API routes and controllers.
  - **use_cases**: Task-related use cases.
- **migrations**: Database migration scripts.
- **tests**: Unit and integration tests.

## 🚀 Project Setup

### 1. Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Python 3.8+](https://www.python.org/downloads/)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/todo-list-service.git
cd todo-list-service
```

### 3. Configure the Database with Docker
Use Docker Compose to spin up a PostgreSQL instance:

```bash
docker-compose up -d
```

### 4. Configure the Python Environment
Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 5. Configure the Database

Create a .env file at the root of the project with the following environment variables:

```plaintext
# Environment
APP_MODULE=app.main:app
APP_ENV=development
PYTHONPATH=.

# Database
POSTGRES_DB=todo_list
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_PASSWORD=todo_password
POSTGRES_USER=todo_user
```

Create the tables in the database using Alembic migrations.

```bash
alembic init migrations
alembic upgrade head
```

### 6. Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000.

### 7. Run the Tests

Run the unit tests to ensure everything is functioning correctly:

```bash
pytest
```

## 📚 API Documentation

The API documentation can be accessed via Swagger, which will be available at the URL: http://localhost:8000/docs.

## 🛠️ Technologies Used

FastAPI - Modern, fast (high-performance), web framework for building APIs with Python 3.6+.
PostgreSQL - Relational database used for data persistence.
SQLAlchemy - ORM used for interacting with the database.
Alembic - Database migration management tool.
Docker - Platform for creating and managing containers.
Pytest - Testing framework for Python.

## 🧑‍💻 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project is licensed under the MIT License.