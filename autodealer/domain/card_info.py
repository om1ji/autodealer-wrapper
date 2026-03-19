"""SQLAlchemy 2.0 ORM model for the card_info table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CardInfo(Base):
    __tablename__ = "card_info"

    card_info_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    visit_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    reg_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    blocked: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="0.00")
    summa_service: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="0.00")
    summa_bonus: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="0.00")
