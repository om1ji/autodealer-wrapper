"""SQLAlchemy 2.0 ORM model for the online_store_order_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OnlineStoreOrderType(Base):
    __tablename__ = "online_store_order_type"

    online_store_order_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
