from fastapi import APIRouter, Depends
from . import crud
from .schemas import Category, CategoryCreate
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Categories"])


@router.post("/", response_model=Category)
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_category(
        session=session,
        category_create=category_create,
    )


@router.get("/", response_model=list[Category])
async def get_categories(
    user_id: int,
    session=Depends(db_helper.session_dependency),
):
    return await crud.get_user_categories(session=session, user_id=user_id)
