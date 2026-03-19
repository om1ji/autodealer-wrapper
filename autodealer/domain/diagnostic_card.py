"""SQLAlchemy 2.0 ORM model for the diagnostic_card table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCard(Base):
    __tablename__ = "diagnostic_card"

    diagnostic_card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    diagnostic_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_tree.diagnostic_tree_id"), nullable=True)
    model_doc_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("identification_doc.identification_doc_id"), nullable=True)
    diagnostic_controller_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_controller.diagnostic_controller_id"), nullable=True)
    proprietor_model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    proprietor_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    proprietor_doc_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("identification_doc.identification_doc_id"), nullable=True)
    representative_model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    representative_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    representative_doc_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("identification_doc.identification_doc_id"), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
    date_diagnostic: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    trust: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    date_repeat: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    conclusion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="-1")
    coupon: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    correct: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    primary_check: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    diagnostic_document_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_document.diagnostic_document_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    document_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=True)
    proprietor_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    organization_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    organization_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    card_version: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    diagnostic_card_pattern_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_card_pattern.diagnostic_card_pattern_id"), nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    car_run: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    car_tyre: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    diagnostic_card_number: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    eaisto_send_state: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    eaisto_card_number: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    rsa_card_number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    tachograph_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    tachograph_brand: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    tachograph_model: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    tachograph_serial_number: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    flag: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="8")
