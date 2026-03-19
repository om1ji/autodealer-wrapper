"""SQLAlchemy 2.0 ORM model for the cloud_abcp_orders table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudAbcpOrders(Base):
    __tablename__ = "cloud_abcp_orders"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    new_orders_count: Mapped[int] = mapped_column(Integer, primary_key=True)
    office_id: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default="0")
