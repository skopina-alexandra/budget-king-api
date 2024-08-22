from fastapi import APIRouter, Depends, status
from . import crud
from .schemas import Record, RecordCreate, RecordUpdate
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["Records"])


@router.post(
    "/",
    response_model=Record,
    status_code=status.HTTP_201_CREATED,
)
async def create_record(
    record_create: RecordCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_record(
        session=session,
        record_create=record_create,
    )
