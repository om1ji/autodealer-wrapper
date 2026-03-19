"""SQLAlchemy 2.0 ORM model for the goods_out_client table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOutClient(Base):
    __tablename__ = "goods_out_client"

    goods_out_client_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    goods_count: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
