"""SQLAlchemy 2.0 ORM model for the client_cache table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ClientCache(Base):
    __tablename__ = "client_cache"

    client_cache_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    last_visit: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    summ_visit: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    count_visit: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    first_visit: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
