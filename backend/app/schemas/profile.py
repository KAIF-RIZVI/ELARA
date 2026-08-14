from pydantic import BaseModel, ConfigDict, Field
from typing import Any
import uuid

class DeveloperProfileBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    display_name: str | None = None
    username: str | None = None
    
    bio: str | None = None
    company: str | None = None
    organization: str | None = None
    designation: str | None = None
    primary_role: str | None = None
    current_company: str | None = None
    current_position: str | None = None
    experience_years: int | None = None
    location: str | None = None
    timezone: str | None = None
    
    primary_language: str | None = None
    preferred_languages: str | None = None
    
    tech_stack: dict[str, Any] | None = None
    frameworks: dict[str, Any] | None = None
    databases: dict[str, Any] | None = None
    cloud_platforms: dict[str, Any] | None = None
    devops_tools: dict[str, Any] | None = None
    ai_ml_technologies: dict[str, Any] | None = None
    areas_of_expertise: dict[str, Any] | None = None
    skills: dict[str, Any] | None = None
    certifications: dict[str, Any] | None = None
    
    github_username: str | None = None
    github_user_id: str | None = None
    github_avatar_url: str | None = None
    github_public_repos: int | None = None
    github_profile_url: str | None = None
    twitter_username: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None
    website: str | None = None

class DeveloperProfileCreate(DeveloperProfileBase):
    pass

class DeveloperProfileUpdate(DeveloperProfileBase):
    pass

class DeveloperProfileResponse(DeveloperProfileBase):
    id: uuid.UUID
    user_id: uuid.UUID
    profile_completion_percentage: int = 0
    open_assignments: int = 0
    availability: str | None = None
    available_for_assignment: bool = True
    open_to_collaboration: bool = True
    
    model_config = ConfigDict(from_attributes=True)

class QuickStats(BaseModel):
    repositories_connected: int
    repositories_indexed: int
    bugs_assigned: int
    ai_recommendations_received: int
    ai_recommendations_accepted: int
    workspace_joined: str | None
    recent_activity_count: int

class AccountInfo(BaseModel):
    user_id: uuid.UUID
    email: str
    account_type: str
    auth_method: str
    workspace_name: str | None
    workspace_role: str | None
    subscription_plan: str | None
    member_since: str | None
    last_login: str | None
    account_status: str
    email_verification_status: bool
    avatar_url: str | None = None

class ConnectedAccounts(BaseModel):
    google_connected: bool
    github_connected: bool
    gitlab_connected: bool
    microsoft_connected: bool

class EnterpriseProfileResponse(BaseModel):
    profile: DeveloperProfileResponse
    account: AccountInfo
    connected_accounts: ConnectedAccounts
    stats: QuickStats

class PublicProfileResponse(BaseModel):
    user_id: uuid.UUID
    full_name: str | None = None
    avatar_url: str | None = None
    organization_role: str | None = None
    developer_title: str | None = None
    bio: str | None = None
    location: str | None = None
    timezone: str | None = None
    skills: dict[str, Any] | None = None
    github_username: str | None = None
    repositories_connected: int = 0
    projects_participated: int = 0
    assigned_bugs: int = 0
    resolved_bugs: int = 0
    developer_score: int = 0
    joined_at: str | None = None
    last_active: str | None = None
    availability_status: str | None = None

    model_config = ConfigDict(from_attributes=True)