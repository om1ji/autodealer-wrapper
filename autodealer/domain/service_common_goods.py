"""SQLAlchemy 2.0 ORM model for the service_common_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceCommonGoods(Base):
    __tablename__ = "service_common_goods"

    service_common_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_common_goods_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_common_goods_tree.service_common_goods_tree_id"), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    unit_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    default_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True, server_default="0")
    ac_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    audatex_uid: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
