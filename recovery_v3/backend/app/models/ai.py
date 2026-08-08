import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Integer, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import WorkspaceEntityBase

class RecStatus(str, enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"

class Recommendation(WorkspaceEntityBase):
    __tablename__ = "recommendations"

    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    status: Mapped[RecStatus] = mapped_column(SQLEnum(RecStatus), default=RecStatus.PENDING, nullable=False)
    attempt: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    
    llm_context: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    localized_modules: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    model_version: Mapped[str] = mapped_column(String, nullable=False)
    units_charged: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

class RecommendationCandidate(WorkspaceEntityBase):
    __tablename__ = "recommendation_candidates"

    recommendation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("recommendations.id", ondelete="CASCADE"), nullable=False, index=True)
    developer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("developer_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    
    rank: Mapped[int] = mapped_column(Integer, nullable=False)
    total_score: Mapped[float] = mapped_column(Float, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    signal_breakdown: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

class Explanation(WorkspaceEntityBase):
    __tablename__ = "explanations"

    candidate_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("recommendation_candidates.id", ondelete="CASCADE"), nullable=False, index=True)
    rationale_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    factors: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    s3_artifact_key: Mapped[str | None] = mapped_column(String, nullable=True)

class AssignStatus(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Assignment(WorkspaceEntityBase):
    __tablename__ = "assignments"

    recommendation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("recommendations.id", ondelete="CASCADE"), nullable=False, index=True)
    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    developer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    approved_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    status: Mapped[AssignStatus] = mapped_column(SQLEnum(AssignStatus), default=AssignStatus.PENDING, nullable=False)
    assigned_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
