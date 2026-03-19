"""SQLAlchemy 2.0 ORM model for the cloud_shop_param table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudShopParam(Base):
    __tablename__ = "cloud_shop_param"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    shop_price_list_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price_column_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
