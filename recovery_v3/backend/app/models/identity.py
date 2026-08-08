import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase, WorkspaceEntityBase

class User(AuditBase):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)
    password_hash: Mapped[str | None] = mapped_column(String, nullable=True) # None for OAuth users
    email_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    last_login_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_deleted: Mapped[bool] = mapped_column(default=False, nullable=False)
    deleted_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)

class OAuthAccount(AuditBase):
    __tablename__ = "oauth_accounts"
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    provider: Mapped[str] = mapped_column(String, nullable=False, index=True) # "google", "github"
    provider_user_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    encrypted_access_token: Mapped[str | None] = mapped_column(String, nullable=True)
    encrypted_refresh_token: Mapped[str | None] = mapped_column(String, nullable=True)
    scopes: Mapped[str | None] = mapped_column(String, nullable=True)
    expires_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class UserSession(AuditBase):
    __tablename__ = "user_sessions"
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    refresh_token_hash: Mapped[str] = mapped_column(String, nullable=False)
    refresh_token_version: Mapped[int] = mapped_column(default=1, nullable=False)
    user_agent: Mapped[str | None] = mapped_column(String, nullable=True)
    device_type: Mapped[str | None] = mapped_column(String, nullable=True)
    device_name: Mapped[str | None] = mapped_column(String, nullable=True)
    browser: Mapped[str | None] = mapped_column(String, nullable=True)
    operating_system: Mapped[str | None] = mapped_column(String, nullable=True)
    ip_address: Mapped[str | None] = mapped_column(String, nullable=True)
    city: Mapped[str | None] = mapped_column(String, nullable=True)
    country: Mapped[str | None] = mapped_column(String, nullable=True)
    last_activity: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    expires_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_revoked: Mapped[bool] = mapped_column(default=False, nullable=False)

class MemberRole(str, enum.Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DEVELOPER = "DEVELOPER"
    SUPPORT = "SUPPORT"
    VIEWER = "VIEWER"

class MemberStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INVITED = "INVITED"
    REVOKED = "REVOKED"

class WorkspaceMember(WorkspaceEntityBase):
    __tablename__ = "workspace_members"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role: Mapped[MemberRole] = mapped_column(SQLEnum(MemberRole), default=MemberRole.DEVELOPER, nullable=False)
    status: Mapped[MemberStatus] = mapped_column(SQLEnum(MemberStatus), default=MemberStatus.ACTIVE, nullable=False)
    joined_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_seen_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class InvitationStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"

class WorkspaceInvitation(WorkspaceEntityBase):
    __tablename__ = "workspace_invitations"

    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    token: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    role: Mapped[MemberRole] = mapped_column(SQLEnum(MemberRole), default=MemberRole.DEVELOPER, nullable=False)
    status: Mapped[InvitationStatus] = mapped_column(SQLEnum(InvitationStatus), default=InvitationStatus.PENDING, nullable=False)
    expires_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    # invited_by and invited_at are natively provided by AuditBase (created_by, created_at) inherited through WorkspaceEntityBase

class APIKey(WorkspaceEntityBase):
    __tablename__ = "api_keys"

    key_hash: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    label: Mapped[str] = mapped_column(String, nullable=False)
    scopes: Mapped[str] = mapped_column(String, nullable=False)
    last_used_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)