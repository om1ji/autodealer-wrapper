"""SQLAlchemy 2.0 ORM model for the goods_out_marking table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import BigInteger, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOutMarking(Base):
    __tablename__ = "goods_out_marking"

    goods_out_marking_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=False)
    marking_code: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    no_scan: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    estimated_status: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    online_validation_result: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    quantity: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    crpt_request_uuid: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    crpt_request_time: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    crpt_min_price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    crpt_max_price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    crpt_error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    crpt_check_status: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    crpt_lm_instance: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    crpt_lm_version: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
