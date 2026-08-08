import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase, WorkspaceEntityBase

class User(AuditBase):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    auth_provider: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[str | None] = mapped_column(String, nullable=True) # None for OAuth users

class MemberRole(str, enum.Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DEVELOPER = "DEVELOPER"

class MemberStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INVITED = "INVITED"
    REVOKED = "REVOKED"

class WorkspaceMember(WorkspaceEntityBase):
    __tablename__ = "workspace_members"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    role: Mapped[MemberRole] = mapped_column(SQLEnum(MemberRole), default=MemberRole.DEVELOPER, nullable=False)
    status: Mapped[MemberStatus] = mapped_column(SQLEnum(MemberStatus), default=MemberStatus.ACTIVE, nullable=False)
    joined_at: Mapped[str | None] = mapped_column(String, nullable=True)

class APIKey(WorkspaceEntityBase):
    __tablename__ = "api_keys"

    key_hash: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    label: Mapped[str] = mapped_column(String, nullable=False)
    scopes: Mapped[str] = mapped_column(String, nullable=False)
    last_used_at: Mapped[str | None] = mapped_column(String, nullable=True)
    revoked_at: Mapped[str | None] = mapped_column(String, nullable=True)
