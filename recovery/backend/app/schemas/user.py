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
    name: str

class UserCreate(UserBase):
    password: str
    auth_provider: str = "local"

class UserResponse(UserBase):
    id: uuid.UUID
    auth_provider: str

    model_config = ConfigDict(from_attributes=True)
