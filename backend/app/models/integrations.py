import uuid
import enum
from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, Enum as SQLEnum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import AuditBase

class Integration(AuditBase):
    __tablename__ = "integrations"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    
    platform: Mapped[str] = mapped_column(String, nullable=False, index=True) # "github", "gitlab", "jira", "slack"
    platform_account_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    
    encrypted_token: Mapped[str] = mapped_column(String, nullable=False)
    scopes: Mapped[str | None] = mapped_column(String, nullable=True)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

class IntegrationStatus(str, enum.Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    REVOKED = "REVOKED"
    ERROR = "ERROR"

class GitHubIntegration(AuditBase):
    __tablename__ = "github_integrations"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    provider: Mapped[str] = mapped_column(String, default="github", nullable=False)
    
    github_installation_id: Mapped[str | None] = mapped_column(String, nullable=True)
    github_account_id: Mapped[str | None] = mapped_column(String, nullable=True)
    github_account_login: Mapped[str | None] = mapped_column(String, nullable=True)
    
    status: Mapped[IntegrationStatus] = mapped_column(SQLEnum(IntegrationStatus), default=IntegrationStatus.CONNECTED, nullable=False)
    
    installed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        UniqueConstraint("organization_id", "provider", name="uix_organization_provider"),
    )