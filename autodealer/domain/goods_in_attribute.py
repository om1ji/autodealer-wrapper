"""SQLAlchemy 2.0 ORM model for the goods_in_attribute table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsInAttribute(Base):
    __tablename__ = "goods_in_attribute"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    goods_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), primary_key=True)
