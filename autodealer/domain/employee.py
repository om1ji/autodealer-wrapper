"""SQLAlchemy 2.0 ORM model for the employee table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Employee(Base):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    firstname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    middlename: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    lastname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(92), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(94), nullable=True)
    birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    sex: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    signature: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    bar_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    inn: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    extention_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
