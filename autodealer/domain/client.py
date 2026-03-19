"""SQLAlchemy 2.0 ORM model for the client table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Client(Base):
    __tablename__ = "client"

    client_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    client_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client_tree.client_tree_id"), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    inn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    kpp: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    sex: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    face: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="-1")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    date_payment: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    price_cost_num: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="1")
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    okpo: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    reminder_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    reminder_active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    reminder_switch: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_norm.price_norm_id"), nullable=True)
    salutation: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    questionary_active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    guid: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    autodealer_web_active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    search_value_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
