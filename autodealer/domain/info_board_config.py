"""SQLAlchemy 2.0 ORM model for the info_board_config table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class InfoBoardConfig(Base):
    __tablename__ = "info_board_config"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    show_managers: Mapped[int] = mapped_column(SmallInteger, primary_key=True, server_default="0")
    show_ad: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    show_ticker: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    ticker: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    ad_display_freq: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="1")
