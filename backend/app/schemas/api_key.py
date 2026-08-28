import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class APIKeyCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)

class APIKeyResponse(BaseModel):
    id: uuid.UUID
    name: str
    prefix: str
    organization_id: uuid.UUID
    workspace_id: uuid.UUID
    created_at: datetime
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
    created_by: Optional[uuid.UUID] = None
    
    model_config = ConfigDict(from_attributes=True)

class APIKeyCreateResponse(APIKeyResponse):
    raw_key: str = Field(
        ..., 
        description="The plaintext API key. This is returned EXACTLY ONCE upon creation and must be stored securely by the client."
    )
