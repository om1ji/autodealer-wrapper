"""SQLAlchemy 2.0 ORM model for the goods_out table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOut(Base):
    __tablename__ = "goods_out"

    goods_out_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_in_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    cost: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    discount: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    goods_count: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False, server_default="0")
    goods_count_fact: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False, server_default="0")
    goods_count_return: Mapped[Decimal] = mapped_column(Numeric(18, 3), nullable=False, server_default="0")
    guarante: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    discount_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    action_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_goods.action_goods_id"), nullable=True)
    discount_manual: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    correction_summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    action_promotion_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_promotion.action_promotion_id"), nullable=True)
    transfer_state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    request_employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    confirmation_employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
