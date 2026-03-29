import os
from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

_engine: Engine | None = None


def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(DATABASE_URL)
    return _engine
