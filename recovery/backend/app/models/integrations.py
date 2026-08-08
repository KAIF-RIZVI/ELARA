import uuid
from sqlalchemy import String, ForeignKey, DateTime
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
    expires_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)