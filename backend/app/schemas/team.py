from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TeamBase(BaseModel):
    name: str
    description: str | None = None

class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    lead_id: uuid.UUID | None = None

class TeamResponse(TeamBase):
    id: uuid.UUID
    organization_id: uuid.UUID
    lead_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
    
    # UI joined fields
    members_count: int = 0
    lead_name: str | None = None

    model_config = ConfigDict(from_attributes=True)