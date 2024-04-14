from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    # created_at: datetime


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
