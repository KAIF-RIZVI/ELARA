import uuid
from typing import List, Optional, Any
from pydantic import BaseModel
from enum import Enum

class OrganizationDashboardStats(BaseModel):
    members_total: int
    members_active: int
    projects_total: int
    projects_active: int
    repositories_total: int
    repositories_indexed: int
    bugs_open: int
    bugs_critical: int

class DashboardProject(BaseModel):
    id: uuid.UUID
    name: str
    status: str
    progress: int
    repository_name: Optional[str]
    open_bugs: int
    last_activity_at: Optional[str]

class DashboardRepository(BaseModel):
    id: uuid.UUID
    full_name: str
    provider: str
    last_synced_at: Optional[str]
    index_status: str
    language: Optional[str]
    visibility: str
    ai_ready: bool

class DashboardBug(BaseModel):
    id: uuid.UUID
    title: str
    priority: str
    severity: str
    status: str
    assigned_developer_name: Optional[str]
    assigned_developer_avatar: Optional[str]
    created_at: str

class DashboardMember(BaseModel):
    user_id: uuid.UUID
    full_name: Optional[str]
    avatar_url: Optional[str]
    role: str
    availability_status: Optional[str]
    developer_score: int

class DashboardActivityType(str, Enum):
    invitation_created = "invitation_created"
    invitation_accepted = "invitation_accepted"
    invitation_revoked = "invitation_revoked"
    member_joined = "member_joined"
    project_created = "project_created"
    repository_connected = "repository_connected"
    repository_disconnected = "repository_disconnected"
    bug_created = "bug_created"
    bug_assigned = "bug_assigned"
    bug_closed = "bug_closed"
    ai_analysis_completed = "ai_analysis_completed"

class DashboardActivity(BaseModel):
    id: uuid.UUID
    type: DashboardActivityType
    actor: Optional[str]
    actor_avatar: Optional[str]
    title: str
    description: str
    created_at: str

class DashboardAIStatus(BaseModel):
    graphcodebert_status: str
    semantic_search_status: str
    fusion_engine_status: str
    developer_recommendation_status: str
    llm_analysis_status: str
    repository_intelligence_status: str

class OrganizationDashboardResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    avatar: Optional[str]
    description: Optional[str]
    created_at: str
    updated_at: str
    last_activity_at: Optional[str]
    owner: str
    member_count: int
    project_count: int
    repository_count: int
    pending_invitation_count: int
    active_status: str
    statistics: OrganizationDashboardStats
    recent_activity: List[DashboardActivity]
