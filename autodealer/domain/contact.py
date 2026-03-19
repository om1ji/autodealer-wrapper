"""SQLAlchemy 2.0 ORM model for the contact table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Contact(Base):
    __tablename__ = "contact"

    contact_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_link_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    zipcode: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    district: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    town: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    street: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    house: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    building: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    flat: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    face: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    phone: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    fax: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    www: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    icq: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    default_contact: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    mobile: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    allow_sms: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    allow_email: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    contact_full: Mapped[Optional[str]] = mapped_column(String(499), nullable=True)
    contact_person_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    search_value_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    preferred_delivery_channel: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    district_code: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("district.code"), nullable=True)
    adr_uuid: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    municipal_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    municipal_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
