"""Simple migration runner that applies SQL files using the project's async engine.

Usage:
    python -m migrations.apply_migrations
or
    python migrations/apply_migrations.py
"""

import asyncio
from pathlib import Path

from core import database


MIGRATIONS_DIR = Path(__file__).parent


async def apply_migration(path: Path) -> None:
    sql = path.read_text()
    engine = database.async_engine
    async with engine.begin() as conn:
        # Split the file into individual statements and execute each.
        # asyncpg (used by SQLAlchemy's asyncpg dialect) cannot prepare
        # multiple statements at once, so execute them separately.
        for stmt in (s.strip() for s in sql.split(";") if s.strip()):
            await conn.exec_driver_sql(stmt)


async def main() -> None:
    # Apply migrations in filename order
    files = sorted(MIGRATIONS_DIR.glob("*.sql"))
    for f in files:
        print(f"Applying migration: {f.name}")
        await apply_migration(f)
    print("Migrations applied successfully.")


if __name__ == "__main__":
    asyncio.run(main())
