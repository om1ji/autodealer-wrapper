"""SQLAlchemy 2.0 ORM model for the card_bonus_operation table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CardBonusOperation(Base):
    __tablename__ = "card_bonus_operation"

    card_bonus_operation_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("card_info.card_info_id"), nullable=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    summa_bonus: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    date_bonus: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("card_bonus_operation.card_bonus_operation_id"), nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
