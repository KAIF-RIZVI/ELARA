from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
import uuid
from app.models.organization import (
    OrganizationStatus,
    OrganizationRole,
    OrganizationInvitationStatus,
    JoinPolicy,
    JoinRequestStatus
)

class OrganizationBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
    industry: Optional[str] = None
    company_size: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[str] = None
    industry: Optional[str] = None
    company_size: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[str] = None
    discoverable: Optional[bool] = None
    join_policy: Optional[JoinPolicy] = None

class OrganizationResponse(OrganizationBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    status: OrganizationStatus
    discoverable: bool
    join_policy: JoinPolicy
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class OrganizationSwitcherResponse(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    logo_url: Optional[str] = None
    organization_status: OrganizationStatus
    subscription_plan: Optional[str] = None
    user_role: OrganizationRole
    member_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class OrganizationMemberUpdate(BaseModel):
    role: OrganizationRole | None = None
    status: str | None = None

class OrganizationDiscoveryResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    logo_url: Optional[str] = None
    tagline: Optional[str] = None
    member_count: int
    join_policy: JoinPolicy
    owner_name: Optional[str] = None
    user_relation: Optional[str] = "NONE" # "MEMBER", "PENDING_REQUEST", or "NONE"

    model_config = ConfigDict(from_attributes=True)

class OrganizationJoinRequestCreate(BaseModel):
    message: Optional[str] = None

class OrganizationJoinRequestResponse(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    user_id: uuid.UUID
    message: Optional[str] = None
    status: JoinRequestStatus
    created_at: datetime
    reviewed_at: Optional[datetime] = None
    
    # Extra fields for dashboard display
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    user_avatar: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class OrganizationMemberResponse(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    user_id: uuid.UUID
    role: OrganizationRole
    status: str
    created_at: datetime
    
    # Joined user data
    full_name: str | None = None
    email: str | None = None
    avatar_url: str | None = None
    
    model_config = ConfigDict(from_attributes=True)

class OrganizationInviteCreate(BaseModel):
    email: str
    role: OrganizationRole = OrganizationRole.DEVELOPER

class OrganizationInviteResponse(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    email: str
    role: OrganizationRole
    status: OrganizationInvitationStatus
    expires_at: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class OrganizationSettingsUpdate(BaseModel):
    default_timezone: str | None = None
    default_language: str | None = None
    allow_member_invites: bool | None = None
    allowed_login_providers: list[str] | None = None
    session_timeout_minutes: int | None = None
    ai_enabled: bool | None = None
    embedding_provider: str | None = None
    llm_provider: str | None = None
    ai_defaults: dict | None = None
    default_repository_settings: dict | None = None
    default_branch: str | None = None
    github_integration_enabled: bool | None = None
    gitlab_integration_enabled: bool | None = None
    azure_devops_integration_enabled: bool | None = None

class OrganizationSettingsResponse(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    default_timezone: str
    default_language: str
    allow_member_invites: bool
    allowed_login_providers: list[str]
    session_timeout_minutes: int
    ai_enabled: bool
    embedding_provider: str
    llm_provider: str
    ai_defaults: dict
    default_repository_settings: dict
    default_branch: str
    github_integration_enabled: bool
    gitlab_integration_enabled: bool
    azure_devops_integration_enabled: bool
    
    model_config = ConfigDict(from_attributes=True)

class OrganizationAuditLogResponse(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    actor_id: uuid.UUID | None
    event_type: str
    resource_type: str
    resource_id: str
    old_values: dict | None
    new_values: dict | None
    metadata_json: dict | None
    ip_address: str | None
    user_agent: str | None
    created_at: datetime
    
    actor_name: str | None = None
    actor_email: str | None = None

    model_config = ConfigDict(from_attributes=True)

class OrganizationStatsResponse(BaseModel):
    projects_count: int
    repositories_count: int
    members_count: int
    teams_count: int
    open_bugs_count: int
    closed_bugs_count: int
    indexed_repositories_count: int
    ai_usage_count: int
    storage_used_bytes: int
    seat_usage: int
    seat_limit: int
