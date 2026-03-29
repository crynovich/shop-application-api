import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)


load_dotenv()

DATABASE_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    db=os.getenv("DB_NAME"),
)

_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        _engine = create_async_engine(DATABASE_URL)
    return _engine


async_engine = get_engine()

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
