"""SQLAlchemy 2.0 ORM model for the service_goods_addon table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceGoodsAddon(Base):
    __tablename__ = "service_goods_addon"

    service_goods_addon_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    unit_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    discount_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    ac_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    audatex_uid: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    correction_summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    returned: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
