from pydantic import BaseModel, ConfigDict


class PlanningBase(BaseModel):
    user_id: int
    category_id: int
    period_id: int
    amount: int
