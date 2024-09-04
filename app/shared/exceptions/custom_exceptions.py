from fastapi import HTTPException


class BusinessException(HTTPException):
    def __init__(self, detail: str = "Business rule violated"):
        super().__init__(status_code=400, detail=detail)


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)
