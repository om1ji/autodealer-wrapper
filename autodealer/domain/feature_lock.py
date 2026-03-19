"""SQLAlchemy 2.0 ORM model for the feature_lock table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class FeatureLock(Base):
    __tablename__ = "feature_lock"

    feature_lock_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_uuid: Mapped[str] = mapped_column(String(100), nullable=False)
