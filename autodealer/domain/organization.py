"""SQLAlchemy 2.0 ORM model for the organization table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Organization(Base):
    __tablename__ = "organization"

    organization_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    face: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    inn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    kpp: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    date_closing_period: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    logo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    date_payment: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    nds: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    order_out: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    tax_schemes_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=True)
    okpo: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    tax_schemes_service_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=True)
    service_guarantee: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    rst_text: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    rst_show: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    ogrn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    can_sale: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    can_buy: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    sale_client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    sale_provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    show_document_in_closing_period: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    diagnostic_operator_num: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    diagnostic_operator_attestate: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    print_check: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    individual_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    individual_requisite: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    diagnostic_operator_pto_num: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    stamp: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    tax_schemes_prepayment_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=True)
    commercialname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    contact_info: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    coord_latitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    coord_longitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    field_activity: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    tax_schemes_supplier_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=True)
    crpt_token: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    crpt_token_valid_to: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    crpt_true_api_token: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    crpt_true_api_token_valid_to: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
