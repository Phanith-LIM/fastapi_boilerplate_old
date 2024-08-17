from pydantic import BaseModel
from typing import Any, List, Optional


class StandardResponse(BaseModel):
    statusCode: int
    message: str
    data: Optional[Any] = None
    errors: Optional[List[dict]] = None
