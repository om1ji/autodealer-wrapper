"""SQLAlchemy 2.0 ORM model for the price_analysis_tree table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceAnalysisTree(Base):
    __tablename__ = "price_analysis_tree"

    price_analysis_tree_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
