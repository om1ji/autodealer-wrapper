"""SQLAlchemy 2.0 ORM model for the model_link table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ModelLink(Base):
    __tablename__ = "model_link"

    model_link_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    model_detail_id: Mapped[int] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    default_car: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    run_average_day: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
