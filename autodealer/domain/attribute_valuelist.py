"""SQLAlchemy 2.0 ORM model for the attribute_valuelist table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AttributeValuelist(Base):
    __tablename__ = "attribute_valuelist"

    attribute_valuelist_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    attribute_description_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    attribute_value: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
