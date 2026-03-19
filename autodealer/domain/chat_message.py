"""SQLAlchemy 2.0 ORM model for the chat_message table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ChatMessage(Base):
    __tablename__ = "chat_message"

    message_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    message_sender_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    message_deliver_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    message_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, server_default="CURRENT_TIME")
    message_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    message_file: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    message_file_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    readed: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    private: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
