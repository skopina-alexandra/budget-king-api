from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Record
from .schemas import RecordCreate, RecordUpdate
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.utils import fill_model_attributes


async def create_record(
    session: AsyncSession,
    record_create: RecordCreate,
):
    record = Record(**record_create.model_dump())
    session.add(record)
    await session.commit()
    return record


async def update_record(
    session: AsyncSession,
    record: Record,
    record_update: RecordUpdate,
):

    record = fill_model_attributes(
        record,
        record_update,
    )
    await session.commit()
    return record


async def delete_record(
    session: AsyncSession,
    record: Record,
) -> None:
    await session.delete(record)
    await session.commit()
