"""SQLAlchemy 2.0 ORM model for the cloud_abcp_param table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudAbcpParam(Base):
    __tablename__ = "cloud_abcp_param"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    shop_price_list_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price_column_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    upload_time_price: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    next_time_full_resync_brands: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_time_request_brands: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_time_check_new_orders: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    order_options: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    last_time_upload_client_balance: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
