from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

DataT = TypeVar('DataT')

class ErrorDetail(BaseModel):
    code: str
    message: str

class APIResponse(BaseModel, Generic[DataT]):
    success: bool = True
    message: Optional[str] = None
    data: Optional[DataT] = None
    error: Optional[ErrorDetail] = None

class PaginatedData(BaseModel, Generic[DataT]):
    items: list[DataT]
    total: int
    page: int
    size: int
    pages: int
