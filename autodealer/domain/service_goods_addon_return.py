"""SQLAlchemy 2.0 ORM model for the service_goods_addon_return table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceGoodsAddonReturn(Base):
    __tablename__ = "service_goods_addon_return"

    service_goods_addon_return_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    service_goods_addon_id: Mapped[int] = mapped_column(Integer, ForeignKey("service_goods_addon.service_goods_addon_id"), nullable=False)
