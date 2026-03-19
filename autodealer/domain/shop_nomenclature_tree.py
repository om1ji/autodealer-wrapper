"""SQLAlchemy 2.0 ORM model for the shop_nomenclature_tree table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclatureTree(Base):
    __tablename__ = "shop_nomenclature_tree"

    shop_nomenclature_tree_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature_tree.shop_nomenclature_tree_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    cloud_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
