"""SQLAlchemy 2.0 ORM model for the manager_structure table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ManagerStructure(Base):
    __tablename__ = "manager_structure"

    manager_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    manager_id: Mapped[int] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    percent_exec_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tariff: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    main_manager: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    percent_goods: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
