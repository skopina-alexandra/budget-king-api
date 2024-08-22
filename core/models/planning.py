from sqlalchemy import ForeignKey
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Planning(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
    )
    period_id: Mapped[int] = mapped_column(
        ForeignKey("periods.id"),
    )
    amount: Mapped[int]
