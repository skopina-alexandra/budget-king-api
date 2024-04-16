from fastapi import APIRouter, Depends, status
from . import crud
from .schemas import Category, CategoryCreate, CategoryUpdate
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import category_by_id

router = APIRouter(tags=["Categories"])


@router.post(
    "/",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_category(
        session=session,
        category_create=category_create,
    )


@router.get(
    "/",
    response_model=list[Category],
)
async def get_categories(
    user_id: int,
    session=Depends(db_helper.session_dependency),
):
    return await crud.get_user_categories(session=session, user_id=user_id)


@router.patch(
    "/{category_id}/",
    response_model=Category,
)
async def update_category(
    category_update: CategoryUpdate,
    category: Category = Depends(category_by_id),
    session=Depends(db_helper.session_dependency),
):
    return await crud.update_category(
        session=session,
        category=category,
        category_update=category_update,
    )


@router.delete("/{category_id}")
async def delete_category(
    category: Category = Depends(category_by_id),
    session=Depends(db_helper.session_dependency),
):
    return await crud.delete_category(
        session=session,
        category=category,
    )
