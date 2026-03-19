"""SQLAlchemy 2.0 ORM model for the card_discont table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CardDiscont(Base):
    __tablename__ = "card_discont"

    card_discont_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    summ: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    work_discont: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    material_discont: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
