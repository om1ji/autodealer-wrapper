"""SQLAlchemy 2.0 ORM model for the online_store_order table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OnlineStoreOrder(Base):
    __tablename__ = "online_store_order"

    online_store_order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    online_store_order_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("online_store_order_type.online_store_order_type_id"), nullable=False)
    online_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
