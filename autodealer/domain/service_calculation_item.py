"""SQLAlchemy 2.0 ORM model for the service_calculation_item table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceCalculationItem(Base):
    __tablename__ = "service_calculation_item"

    service_calculation_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_calculation_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_calculation_tree.service_calculation_tree_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    model_link_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rt_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rt_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_card_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("card_info.card_info_id"), nullable=True)
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    discount_goods: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    ac_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    ac_map: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    date_create: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    document_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=True, server_default="26")
    flag: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="16")
    rmi_car_select: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
