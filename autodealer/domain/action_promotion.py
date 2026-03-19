"""SQLAlchemy 2.0 ORM model for the action_promotion table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActionPromotion(Base):
    __tablename__ = "action_promotion"

    action_promotion_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
    action_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_goods.action_goods_id"), nullable=True)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
