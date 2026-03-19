"""SQLAlchemy 2.0 ORM model for the shop_nomenclature_photo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclaturePhoto(Base):
    __tablename__ = "shop_nomenclature_photo"

    shop_nomenclature_photo_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    hash: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
