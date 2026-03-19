"""SQLAlchemy 2.0 ORM model for the shop_material_response table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopMaterialResponse(Base):
    __tablename__ = "shop_material_response"

    shop_material_response_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_structure_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_structure.organization_structure_id"), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    store_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("store.store_id"), nullable=True)
