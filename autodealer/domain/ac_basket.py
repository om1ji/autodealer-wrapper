"""SQLAlchemy 2.0 ORM model for the ac_basket table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AcBasket(Base):
    __tablename__ = "ac_basket"

    ac_basket_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ac_basket_group_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("ac_basket_group.ac_basket_group_id"), nullable=True)
    mark_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    model_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    detail_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    detail_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    detail_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    basket_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ac_doc_id: Mapped[int] = mapped_column(Integer, nullable=False)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
