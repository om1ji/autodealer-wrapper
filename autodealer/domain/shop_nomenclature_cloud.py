"""SQLAlchemy 2.0 ORM model for the shop_nomenclature_cloud table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclatureCloud(Base):
    __tablename__ = "shop_nomenclature_cloud"

    shop_nomenclature_cloud_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[int] = mapped_column(Integer, nullable=False)
    cloud_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    cloud_upload_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    cloud_upload_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    clour_offer_invalidate: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    removed: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
