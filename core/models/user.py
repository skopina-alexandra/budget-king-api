from .base import Base
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class User(Base):
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    current_interval: Mapped[int | None] = mapped_column(
        ForeignKey("intervals.id"),
    )
    categories: Mapped[list["Category"]] = relationship(back_populates="user")
