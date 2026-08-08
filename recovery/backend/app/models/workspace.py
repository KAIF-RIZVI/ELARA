import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase, WorkspaceEntityBase

class WorkspaceStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

class Workspace(AuditBase):
    __tablename__ = "workspaces"

    name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    status: Mapped[WorkspaceStatus] = mapped_column(SQLEnum(WorkspaceStatus), default=WorkspaceStatus.ACTIVE, nullable=False)
    settings: Mapped[dict | None] = mapped_column(nullable=True)

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
