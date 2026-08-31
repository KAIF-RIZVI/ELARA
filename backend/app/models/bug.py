import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Integer, Text, DateTime, JSON, Boolean, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.core.base_model import AuditBase

class BugSource(str, enum.Enum):
    MANUAL = "MANUAL"
    API = "API"
    INTEGRATION = "INTEGRATION"

class BugState(str, enum.Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    BLOCKED = "BLOCKED"
    RESOLVED = "RESOLVED"
    VERIFIED = "VERIFIED"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"
    DUPLICATE = "DUPLICATE"
    WONT_FIX = "WONT_FIX"

class BugSeverity(str, enum.Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class BugPriority(str, enum.Enum):
    P0 = "P0" # Critical / Blocker
    P1 = "P1" # High
    P2 = "P2" # Medium
    P3 = "P3" # Low
    P4 = "P4" # Backlog

class Bug(AuditBase):
    __tablename__ = "bugs"
    __table_args__ = (
        CheckConstraint("(workspace_id IS NULL) <> (organization_id IS NULL)", name="chk_bug_owner"),
    )

    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    
    project_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("projects.id", ondelete="SET NULL"), nullable=True, index=True)
    repository_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("repositories.id", ondelete="SET NULL"), nullable=True, index=True)
    
    source: Mapped[BugSource] = mapped_column(SQLEnum(BugSource), default=BugSource.MANUAL, nullable=False)
    external_ref: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
    
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    stack_trace: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    state: Mapped[BugState] = mapped_column(SQLEnum(BugState), default=BugState.OPEN, nullable=False)
    severity: Mapped[BugSeverity] = mapped_column(SQLEnum(BugSeverity), default=BugSeverity.MEDIUM, nullable=False)
    priority: Mapped[BugPriority] = mapped_column(SQLEnum(BugPriority), default=BugPriority.P2, nullable=False)
    
    # Detailed Context Fields
    environment: Mapped[dict | None] = mapped_column(JSONB, nullable=True) # e.g. OS, Browser, App Version
    reproduction_steps: Mapped[str | None] = mapped_column(Text, nullable=True)
    expected_behavior: Mapped[str | None] = mapped_column(Text, nullable=True)
    actual_behavior: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    category: Mapped[str | None] = mapped_column(String, nullable=True)
    
    duplicate_of: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("bugs.id", ondelete="SET NULL"), nullable=True)
    
    # Reporter Information (Can be system user or external payload)
    reported_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    reporter_metadata: Mapped[dict | None] = mapped_column(JSONB, nullable=True) # external email, name etc.

    resolved_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    closed_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    deleted_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class BugAttachment(AuditBase):
    __tablename__ = "bug_attachments"

    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    s3_key: Mapped[str] = mapped_column(String, nullable=False)
    mime_type: Mapped[str] = mapped_column(String, nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)

class BugAssignment(AuditBase):
    __tablename__ = "bug_assignments"
    __table_args__ = (
        CheckConstraint("(workspace_id IS NULL) <> (organization_id IS NULL)", name="chk_bug_assignment_owner"),
    )
    
    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    developer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    assigned_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    assigned_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    removed_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class BugComment(AuditBase):
    __tablename__ = "bug_comments"
    __table_args__ = (
        CheckConstraint("(workspace_id IS NULL) <> (organization_id IS NULL)", name="chk_bug_comment_owner"),
    )
    
    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    author_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    deleted_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class IdempotencyKey(AuditBase):
    __tablename__ = "idempotency_keys"
    __table_args__ = (
        UniqueConstraint("workspace_id", "organization_id", "key", name="uix_workspace_org_key"),
        CheckConstraint("(workspace_id IS NULL) <> (organization_id IS NULL)", name="chk_idempotency_owner"),
    )
    
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    key: Mapped[str] = mapped_column(String, nullable=False, index=True)
    request_hash: Mapped[str] = mapped_column(String, nullable=False)
    bug_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("bugs.id", ondelete="SET NULL"), nullable=True)
    expires_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
