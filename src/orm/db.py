from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from config import DATABASE_URL, SYNC_DATABASE_URL, DEBUG


engine = create_async_engine(DATABASE_URL, echo=DEBUG, future=True)
sync_engine = create_engine(SYNC_DATABASE_URL, echo=DEBUG, future=True)  # for sync query


# for Dependency Injection
async def get_session() -> AsyncSession:
    async with AsyncSession(engine) as session:
        yield session
