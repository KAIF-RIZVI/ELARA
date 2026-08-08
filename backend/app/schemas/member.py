from pydantic import BaseModel, ConfigDict, EmailStr
import uuid
from datetime import datetime
from app.models.identity import MemberRole, MemberStatus, InvitationStatus

class MemberUpdate(BaseModel):
    role: MemberRole | None = None
    status: MemberStatus | None = None

class MemberResponse(BaseModel):
    id: uuid.UUID
    workspace_id: uuid.UUID
    user_id: uuid.UUID
    role: MemberRole
    status: MemberStatus
    joined_at: datetime | None = None
    last_seen_at: datetime | None = None
    
    # Joined data for UI
    full_name: str | None = None
    email: str | None = None
    avatar_url: str | None = None

    model_config = ConfigDict(from_attributes=True)

class InviteCreate(BaseModel):
    email: EmailStr
    role: MemberRole = MemberRole.DEVELOPER

class InviteResponse(BaseModel):
    id: uuid.UUID
    workspace_id: uuid.UUID
    email: str
    role: MemberRole
    status: InvitationStatus
    expires_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)