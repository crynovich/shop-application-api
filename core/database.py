import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        _engine = create_async_engine(DATABASE_URL)
    return _engine


async_engine = get_engine()

async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)
