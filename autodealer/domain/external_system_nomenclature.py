"""SQLAlchemy 2.0 ORM model for the external_system_nomenclature table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ExternalSystemNomenclature(Base):
    __tablename__ = "external_system_nomenclature"

    external_system_nomenclature_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    external_system_type: Mapped[int] = mapped_column(Integer, nullable=False)
    external_system_uid: Mapped[Optional[str]] = mapped_column(String(2039), nullable=True)
