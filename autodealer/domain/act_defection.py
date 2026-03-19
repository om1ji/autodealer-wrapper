"""SQLAlchemy 2.0 ORM model for the act_defection table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActDefection(Base):
    __tablename__ = "act_defection"

    act_defection_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    act_defection_check_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("act_defection_check.act_defection_check_id"), nullable=True)
    model_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    check_register: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    check_passed: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    check_fixed: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    original_document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    check_passed_left: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    check_passed_right: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
