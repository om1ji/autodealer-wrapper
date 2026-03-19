"""SQLAlchemy 2.0 ORM model for the goods_out_manager_structure table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOutManagerStructure(Base):
    __tablename__ = "goods_out_manager_structure"

    manager_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=False)
    manager_id: Mapped[int] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=False)
    percent_goods: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    party: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
