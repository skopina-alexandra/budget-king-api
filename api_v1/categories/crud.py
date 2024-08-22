from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Category
from .schemas import CategoryCreate, CategoryUpdate
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.utils import fill_model_attributes


async def create_category(
    session: AsyncSession,
    category_create: CategoryCreate,
):
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    return category


async def get_category(
    session: AsyncSession,
    category_id: int,
) -> Category | None:
    return await session.get(Category, category_id)


async def get_user_categories(
    session: AsyncSession,
    user_id: int,
) -> list[Category]:
    stmt = select(Category).where(Category.user_id == user_id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryUpdate,
) -> Category:
    category = fill_model_attributes(
        category,
        category_update,
    )
    await session.commit()
    return category


async def delete_category(
    session: AsyncSession,
    category: Category,
) -> None:
    await session.delete(category)
    await session.commit()
