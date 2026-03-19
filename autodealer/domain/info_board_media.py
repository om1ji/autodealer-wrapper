"""SQLAlchemy 2.0 ORM model for the info_board_media table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, LargeBinary, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class InfoBoardMedia(Base):
    __tablename__ = "info_board_media"

    info_board_media_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    picture: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    position_no: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
