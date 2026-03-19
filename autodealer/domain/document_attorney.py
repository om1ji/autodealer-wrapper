"""SQLAlchemy 2.0 ORM model for the document_attorney table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentAttorney(Base):
    __tablename__ = "document_attorney"

    document_attorney_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    organization_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    organization_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=False)
    client_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    client_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    consumer_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    consumer_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    consumer_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    payer_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    payer_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    payer_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=False)
    date_create: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    material_assets: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
    flag: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    date_narad: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    number_narad: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    name_narad: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    job_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("job.job_id"), nullable=True)
