"""SQLAlchemy 2.0 ORM model for the card_bonus table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CardBonus(Base):
    __tablename__ = "card_bonus"

    card_bonus_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    summ: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    goods_factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    work_factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
