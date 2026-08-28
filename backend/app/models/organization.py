import uuid
import enum
from typing import Any
from datetime import datetime, timezone
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase

class OrganizationStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    TRIAL = "TRIAL"
    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    SUSPENDED = "SUSPENDED"
    EXPIRED = "EXPIRED"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    DELETING = "DELETING"

class OrganizationRole(str, enum.Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    DEVELOPER = "DEVELOPER"
    QA_ENGINEER = "QA_ENGINEER"
    REPORTER = "REPORTER"
    VIEWER = "VIEWER"

class JoinPolicy(str, enum.Enum):
    CLOSED = "CLOSED"
    REQUEST_TO_JOIN = "REQUEST_TO_JOIN"
    OPEN = "OPEN"

class JoinRequestStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

class OrganizationInvitationStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REVOKED = "REVOKED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"

class Organization(AuditBase):
    __tablename__ = "organizations"

    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    logo_url: Mapped[str | None] = mapped_column(String, nullable=True)
    website: Mapped[str | None] = mapped_column(String, nullable=True)
    industry: Mapped[str | None] = mapped_column(String, nullable=True)
    company_size: Mapped[str | None] = mapped_column(String, nullable=True)
    country: Mapped[str | None] = mapped_column(String, nullable=True)
    timezone: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[OrganizationStatus] = mapped_column(SQLEnum(OrganizationStatus), default=OrganizationStatus.ACTIVE, nullable=False)
    
    discoverable: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    join_policy: Mapped[JoinPolicy] = mapped_column(SQLEnum(JoinPolicy), default=JoinPolicy.CLOSED, nullable=False)
    tagline: Mapped[str | None] = mapped_column(String, nullable=True)

class OrganizationMember(AuditBase):
    __tablename__ = "organization_members"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role: Mapped[OrganizationRole] = mapped_column(SQLEnum(OrganizationRole), default=OrganizationRole.VIEWER, nullable=False)
    status: Mapped[str] = mapped_column(String, default="ACTIVE", nullable=False)

class OrganizationInvitation(AuditBase):
    __tablename__ = "organization_invitations"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    role: Mapped[OrganizationRole] = mapped_column(SQLEnum(OrganizationRole), nullable=False)
    token_hash: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    status: Mapped[OrganizationInvitationStatus] = mapped_column(SQLEnum(OrganizationInvitationStatus), default=OrganizationInvitationStatus.PENDING, nullable=False)
    invited_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    accepted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

class OrganizationJoinRequest(AuditBase):
    __tablename__ = "organization_join_requests"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    message: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[JoinRequestStatus] = mapped_column(SQLEnum(JoinRequestStatus), default=JoinRequestStatus.PENDING, nullable=False)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

class OrganizationSettings(AuditBase):
    __tablename__ = "organization_settings"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, unique=True)
    default_timezone: Mapped[str] = mapped_column(String, default="UTC", nullable=False)
    default_language: Mapped[str] = mapped_column(String, default="en", nullable=False)
    
    # Security
    allow_member_invites: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    allowed_login_providers: Mapped[list[str]] = mapped_column(JSONB, default=["EMAIL", "GITHUB", "GOOGLE"], nullable=False)
    session_timeout_minutes: Mapped[int] = mapped_column(nullable=False, default=1440)
    
    # AI
    ai_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    embedding_provider: Mapped[str] = mapped_column(String, default="OPENAI", nullable=False)
    llm_provider: Mapped[str] = mapped_column(String, default="OPENAI", nullable=False)
    ai_defaults: Mapped[dict[str, Any]] = mapped_column(JSONB, default={}, nullable=False)
    
    # Developer
    default_repository_settings: Mapped[dict[str, Any]] = mapped_column(JSONB, default={}, nullable=False)
    default_branch: Mapped[str] = mapped_column(String, default="main", nullable=False)
    
    # Git Integrations
    github_integration_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    gitlab_integration_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    azure_devops_integration_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

class OrganizationSubscription(AuditBase):
    __tablename__ = "organization_subscriptions"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, unique=True)
    subscription_plan: Mapped[str] = mapped_column(String, default="FREE", nullable=False)
    subscription_status: Mapped[str] = mapped_column(String, default="ACTIVE", nullable=False)
    seat_limit: Mapped[int] = mapped_column(nullable=False, default=5)
    trial_ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

class OrganizationAuditLog(AuditBase):
    __tablename__ = "organization_audit_logs"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    actor_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    event_type: Mapped[str] = mapped_column(String, nullable=False, index=True)
    resource_type: Mapped[str] = mapped_column(String, nullable=False)
    resource_id: Mapped[str] = mapped_column(String, nullable=False)
    old_values: Mapped[dict[str, Any] | None] = mapped_column(JSONB, nullable=True)
    new_values: Mapped[dict[str, Any] | None] = mapped_column(JSONB, nullable=True)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSONB, nullable=True)
    ip_address: Mapped[str | None] = mapped_column(String, nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String, nullable=True)

class OrganizationEntityBase(AuditBase):
    __abstract__ = True
    
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
