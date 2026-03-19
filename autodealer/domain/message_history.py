"""SQLAlchemy 2.0 ORM model for the message_history table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class MessageHistory(Base):
    __tablename__ = "message_history"

    message_history_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    date_send: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    adres: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    send_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    send_status: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    send_status_text: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    message_theme: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    send_param: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    putoff_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    date_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    document_registry_order_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    external_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    channel: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    channel_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    chat_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    user_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
