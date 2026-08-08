from sqlalchemy import Column, String, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
import enum

from app.core.base_model import AuditBase, WorkspaceEntityBase

if TYPE_CHECKING:
    from app.modules.users.models import User
    from app.modules.projects.models import Project

class WorkspaceStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    READ_ONLY = "READ_ONLY"

class Workspace(AuditBase):
    __tablename__ = "workspaces"

    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    status: Mapped[WorkspaceStatus] = mapped_column(SQLEnum(WorkspaceStatus), default=WorkspaceStatus.ACTIVE, nullable=False)
    settings: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    # Relationships
    members: Mapped[list["WorkspaceMember"]] = relationship("WorkspaceMember", back_populates="workspace", cascade="all, delete-orphan")
    projects: Mapped[list["Project"]] = relationship("Project", back_populates="workspace", cascade="all, delete-orphan")


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

    user_id: Mapped["uuid.UUID"] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    role: Mapped[MemberRole] = mapped_column(SQLEnum(MemberRole), default=MemberRole.DEVELOPER, nullable=False)
    status: Mapped[MemberStatus] = mapped_column(SQLEnum(MemberStatus), default=MemberStatus.ACTIVE, nullable=False)
    
    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="members")
    user: Mapped["User"] = relationship("User", back_populates="workspace_memberships")
