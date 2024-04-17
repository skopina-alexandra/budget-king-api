from .base import Base
from sqlalchemy.orm import Mapped


class Interval(Base):
    value: Mapped[str]
