"""SQLAlchemy 2.0 ORM model for the marking_goods_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class MarkingGoodsType(Base):
    __tablename__ = "marking_goods_type"

    marking_goods_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    goods_type: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    required: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    required_from: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    strict_mode: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    strict_mode_from: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    hash: Mapped[str] = mapped_column(String(50), nullable=False)
