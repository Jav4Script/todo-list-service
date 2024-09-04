from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(_, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": exc.status_code},
    )


async def generic_exception_handler(_, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "code": 500},
    )


async def starlette_exception_handler(_, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": exc.status_code},
    )
