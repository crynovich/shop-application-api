import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)


load_dotenv()

# passwordFile = os.getenv("POSTGRES_PASSWORD_FILE")
# if passwordFile is None:
#     raise RuntimeError("DB PASSWORD NOT CONFIGURED")

# with open(passwordFile, "r") as f:
#     DB_PASSWORD = f.read().strip()

DATABASE_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
    user=os.getenv("POSTGRES_DB_USER"),
    password=os.getenv("POSTGRES_DB_PASSWORD"),
    # password=DB_PASSWORD,
    host=os.getenv("POSTGRES_DB_HOST"),
    port=os.getenv("POSTGRES_DB_PORT"),
    db=os.getenv("POSTGRES_DB"),
)

_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        ssl = os.getenv("POSTGRES_SSL", "false").lower() == "true"
        connect_args = {"ssl": "require"} if ssl else {}
        _engine = create_async_engine(DATABASE_URL, connect_args=connect_args)
    return _engine


async_engine = get_engine()

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
