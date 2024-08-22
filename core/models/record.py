from sqlalchemy import ForeignKey, TIMESTAMP
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy.sql import func


class Record(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
    )
    amount: Mapped[int]
    date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
