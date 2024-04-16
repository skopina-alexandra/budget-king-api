from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Literal, get_args
from sqlalchemy import Enum, ForeignKey

CategoryType = Literal["income", "outcome"]


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str]
    type: Mapped[CategoryType] = mapped_column(
        Enum(
            *get_args(CategoryType),
            name="category_type",
        ),
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
