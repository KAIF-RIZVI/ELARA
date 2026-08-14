import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import WorkspaceEntityBase
