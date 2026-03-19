"""SQLAlchemy 2.0 ORM model for the client_recommended_work table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ClientRecommendedWork(Base):
    __tablename__ = "client_recommended_work"

    client_recommended_work_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    rt_work_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    work_source: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price_norm: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    external_id: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
