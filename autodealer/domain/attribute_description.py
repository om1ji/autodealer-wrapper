"""SQLAlchemy 2.0 ORM model for the attribute_description table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AttributeDescription(Base):
    __tablename__ = "attribute_description"

    attribute_description_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    metatable_id: Mapped[int] = mapped_column(Integer, nullable=False)
    field_caption: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    attribute_position: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    value_type: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    value_s: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    value_i: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    value_r: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    value_d: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    value_b: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    document_type_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    value_d_now: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    value_t: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    value_f: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    value_p: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    required_value: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    value_number: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    delimiter_number: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
