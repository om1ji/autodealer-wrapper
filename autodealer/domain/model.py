"""SQLAlchemy 2.0 ORM model for the model table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Model(Base):
    __tablename__ = "model"

    model_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark_id: Mapped[int] = mapped_column(Integer, ForeignKey("mark.mark_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    rt_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rt_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    category: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    tonnage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    power_engine: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    power_engine_watt: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    place_passenger: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    max_mass: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    empty_mass: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    car_body_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_body_type.car_body_type_id"), nullable=True)
    car_brake_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_brake_type.car_brake_type_id"), nullable=True)
    car_engine_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_engine_type.car_engine_type_id"), nullable=True)
    car_fuel_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_fuel_type.car_fuel_type_id"), nullable=True)
    car_gearbox_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_gearbox_type.car_gearbox_type_id"), nullable=True)
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_norm.price_norm_id"), nullable=True)
