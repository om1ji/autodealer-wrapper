"""SQLAlchemy 2.0 ORM model for the service_work table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceWork(Base):
    __tablename__ = "service_work"

    service_work_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="1")
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="1")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price_norm: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    guarante: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_work_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    rt_work_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    work_source: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    correction_summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    searching_phrase_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("searching_phrase.searching_phrase_id"), nullable=True)
    next_date_work_done: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    service_work_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_work.service_work_id"), nullable=True)
    action_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_goods.action_goods_id"), nullable=True)
    discount_manual: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    action_promotion_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_promotion.action_promotion_id"), nullable=True)
    returned: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    external_id: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
