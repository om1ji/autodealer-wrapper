"""SQLAlchemy 2.0 ORM model for the price_norm table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceNorm(Base):
    __tablename__ = "price_norm"

    price_norm_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
