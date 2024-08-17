from pydantic import BaseModel
from typing import List, Dict, Any


class ErrorDetail(BaseModel):
    field: str
    message: str


class ValidationErrorResponse(BaseModel):
    statusCode: int
    message: str
    errors: List[ErrorDetail]
