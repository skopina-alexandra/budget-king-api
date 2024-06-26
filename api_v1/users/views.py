from fastapi import APIRouter, Depends, status
from . import crud
from .schemas import User, UserCreate
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Users"])


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_user(
        session=session,
        user_create=user_create,
    )
