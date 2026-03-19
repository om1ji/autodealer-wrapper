"""SQLAlchemy 2.0 ORM model for the user_cost_right table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class UserCostRight(Base):
    __tablename__ = "user_cost_right"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), primary_key=True)
    shop_price_list_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_price_list.shop_price_list_id"), nullable=False)
    cost_rigth: Mapped[int] = mapped_column(SmallInteger, nullable=False)
