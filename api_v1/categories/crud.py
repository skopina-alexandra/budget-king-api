from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Category, CategoryType
from .schemas import CategoryCreate
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_category(session: AsyncSession, category_create: CategoryCreate):
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    return category


async def get_user_categories(session: AsyncSession, user_id: int) -> list[Category]:
    stmt = select(Category).where(Category.user_id == user_id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)
