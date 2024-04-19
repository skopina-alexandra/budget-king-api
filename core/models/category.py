from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Literal, get_args
from sqlalchemy import Enum, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

CategoryType = Literal["income", "outcome", "savings"]


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
    user: Mapped["User"] = relationship(back_populates="categories")
