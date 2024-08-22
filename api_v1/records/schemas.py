from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RecordBase(BaseModel):
    user_id: int
    category_id: int
    amount: int
    date: datetime


class Record(RecordBase):
    pass


class RecordCreate(RecordBase):
    pass


class RecordUpdate(RecordBase):
    pass
