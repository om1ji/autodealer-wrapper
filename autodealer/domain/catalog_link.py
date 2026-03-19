"""SQLAlchemy 2.0 ORM model for the catalog_link table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CatalogLink(Base):
    __tablename__ = "catalog_link"

    catalog_link_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    ac_doc_id: Mapped[int] = mapped_column(Integer, nullable=False)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
    ac_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
