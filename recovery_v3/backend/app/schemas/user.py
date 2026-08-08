from typing import Any
from pydantic import BaseModel, EmailStr, ConfigDict
import uuid

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: str | None = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
