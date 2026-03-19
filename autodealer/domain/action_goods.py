"""SQLAlchemy 2.0 ORM model for the action_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActionGoods(Base):
    __tablename__ = "action_goods"

    action_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    date_begin: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    date_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization.organization_id"), nullable=True)
    action_condition: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_days: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    discount_card_condition: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confirm_discount_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confirm_discount: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    action_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
