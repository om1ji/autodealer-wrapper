"""SQLAlchemy 2.0 ORM model for the operation table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Operation(Base):
    __tablename__ = "operation"

    operation_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization.organization_id"), nullable=True)
    manager_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=True)
    state_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation_state.operation_state_id"), nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    client_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation_type.operation_type_id"), nullable=True)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
    date_operation: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    notify_sound: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    alert_enabled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    alert_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    all_day: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    document_registry_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    discount_card_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("card_info.card_info_id"), nullable=True)
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_norm.price_norm_id"), nullable=True)
    rt_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rt_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_goods: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    rmi_car_select: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
