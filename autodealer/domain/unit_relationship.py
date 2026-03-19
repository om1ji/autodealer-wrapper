"""SQLAlchemy 2.0 ORM model for the unit_relationship table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class UnitRelationship(Base):
    __tablename__ = "unit_relationship"

    unit_relationship_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    unit_main_id: Mapped[int] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=False)
    unit_relation_id: Mapped[int] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=False)
    relation: Mapped[float] = mapped_column(Float, nullable=False)
