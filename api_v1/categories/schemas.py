from pydantic import BaseModel, ConfigDict
from core.models import CategoryType


class CategoryBase(BaseModel):
    name: str
    type: CategoryType
    user_id: int


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryCreate):
    name: str | None = None
    type: CategoryType | None = None
    user_id: int | None = None
