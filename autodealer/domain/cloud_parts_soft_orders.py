"""SQLAlchemy 2.0 ORM model for the cloud_parts_soft_orders table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudPartsSoftOrders(Base):
    __tablename__ = "cloud_parts_soft_orders"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    new_orders_count: Mapped[int] = mapped_column(Integer, primary_key=True)
