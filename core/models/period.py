from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy import DateTime, Computed
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Period(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    start: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    interval_id: Mapped[int] = mapped_column(
        ForeignKey("intervals.id"),
    )
