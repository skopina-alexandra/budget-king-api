from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str):
        self.engine = create_async_engine(url=url)
        # self.engine = create_async_engine(url=url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=f"postgresql+asyncpg://{settings.main_db_user}:{settings.main_db_password}@{settings.main_db_host}/{settings.main_db_name}"
)
