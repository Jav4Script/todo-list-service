import ast
import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

from app.shared.infrastructure.exception_handlers import (
    generic_exception_handler,
    http_exception_handler,
    starlette_exception_handler,
)
from app.task.controllers.task_controllers import register_routes

load_dotenv()


def create_app():
    app = FastAPI()

    cors_origins = os.getenv("CORS_ORIGINS", "[]")
    cors_origins = ast.literal_eval(cors_origins)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, starlette_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)

    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8000, reload=os.getenv("APP_ENV") == "development"
    )

# Good practice: Using environment variables for configuration.
# Clean Code: Main entry point is clearly defined.
# KISS: Simple and straightforward application startup logic.
