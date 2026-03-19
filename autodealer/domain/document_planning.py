"""SQLAlchemy 2.0 ORM model for the document_planning table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPlanning(Base):
    __tablename__ = "document_planning"

    document_planning_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    planning_pattern_task_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("planning_pattern_task.planning_pattern_task_id"), nullable=True)
    planning_work_place_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("planning_work_place.planning_work_place_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    client_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    manager_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=True)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    layer: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    date_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    alert_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    alert_enabled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    state: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="32")
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    source_flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    synchronize_service_doc: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    correction_time: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
