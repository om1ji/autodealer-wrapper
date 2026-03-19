"""SQLAlchemy 2.0 ORM model for the currency table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Currency(Base):
    __tablename__ = "currency"

    currency_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    shortname: Mapped[str] = mapped_column(String(5), nullable=False)
    gender: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    word_form_rs: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_r1: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_r2: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_r5: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_ks: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_k1: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_k2: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    word_form_k5: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    national_currency: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
