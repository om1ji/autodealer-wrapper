"""SQLAlchemy 2.0 ORM model for the contract table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Contract(Base):
    __tablename__ = "contract"

    contract_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    default_contract: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    contract_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    contract_type: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
