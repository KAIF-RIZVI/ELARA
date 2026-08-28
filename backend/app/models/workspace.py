import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey
from typing import Any
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase, WorkspaceEntityBase

class WorkspaceStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

class Workspace(AuditBase):
    __tablename__ = "workspaces"

    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, unique=True, index=True)
    owner_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    status: Mapped[WorkspaceStatus] = mapped_column(SQLEnum(WorkspaceStatus), default=WorkspaceStatus.ACTIVE, nullable=False)
    settings: Mapped[dict[str, Any] | None] = mapped_column(JSONB, nullable=True)

    # Subscriptions, AIWallets, APIKeys, Projects, Members will be related via back_populates

class PlanTier(str, enum.Enum):
    FREE = "FREE"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"

class Subscription(WorkspaceEntityBase):
    __tablename__ = "subscriptions"

    plan: Mapped[PlanTier] = mapped_column(SQLEnum(PlanTier), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    current_period_end: Mapped[str | None] = mapped_column(String, nullable=True) # ISO Date

class AIWallet(WorkspaceEntityBase):
    __tablename__ = "ai_wallets"

    balance_units: Mapped[int] = mapped_column(default=0, nullable=False)
    monthly_grant: Mapped[int] = mapped_column(default=0, nullable=False)
    refreshed_at: Mapped[str | None] = mapped_column(String, nullable=True)

class AIUnitTransaction(WorkspaceEntityBase):
    __tablename__ = "ai_unit_transactions"

    wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ai_wallets.id"), nullable=False)
    delta_units: Mapped[int] = mapped_column(nullable=False)
    reason: Mapped[str] = mapped_column(String, nullable=False)
    ref_id: Mapped[uuid.UUID | None] = mapped_column(nullable=True)

class ActivityLog(AuditBase):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    bug_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=True, index=True)

    action: Mapped[str] = mapped_column(String, nullable=False) # e.g. "bug.fixed", "repo.connected"
    target: Mapped[str] = mapped_column(String, nullable=False) # e.g. "auth-service crash on startup"
    status: Mapped[str] = mapped_column(String, nullable=False) # "success", "info", "warning"
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    metadata_payload: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
