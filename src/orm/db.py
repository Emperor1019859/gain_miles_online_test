from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from config import DATABASE_URL, SYNC_DATABASE_URL, DEBUG


engine = create_async_engine(DATABASE_URL, echo=DEBUG, future=True)
sync_engine = create_engine(SYNC_DATABASE_URL, echo=DEBUG, future=True)  # for sync query
