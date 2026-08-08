import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase, WorkspaceEntityBaseclass ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class WorkspaceStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class Workspace(AuditBase):
    __tablename__ = "workspaces"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    logo_url: Mapped[str | None] = mapped_column(String, nullable=True)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    status: Mapped[WorkspaceStatus] = mapped_column(SQLEnum(WorkspaceStatus), default=WorkspaceStatus.ACTIVE, nullable=False)
    settings: Mapped[dict | None] = mapped_column(JSONB, nullable=True)class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)    # Subscriptions, AIWallets, APIKeys, Projects, Members will be related via back_populatesclass ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class PlanTier(str, enum.Enum):
    FREE = "FREE"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class Subscription(WorkspaceEntityBase):
    __tablename__ = "subscriptions"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)    plan: Mapped[PlanTier] = mapped_column(SQLEnum(PlanTier), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    current_period_end: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class AIWallet(WorkspaceEntityBase):
    __tablename__ = "ai_wallets"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)    balance_units: Mapped[int] = mapped_column(default=0, nullable=False)
    monthly_grant: Mapped[int] = mapped_column(default=0, nullable=False)
    refreshed_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)class AIUnitTransaction(WorkspaceEntityBase):
    __tablename__ = "ai_unit_transactions"class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)    wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ai_wallets.id"), nullable=False)
    delta_units: Mapped[int] = mapped_column(nullable=False)
    reason: Mapped[str] = mapped_column(String, nullable=False)
    ref_id: Mapped[uuid.UUID | None] = mapped_column(nullable=True)class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)
