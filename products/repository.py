from sqlalchemy import text

from products.model import Product
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class ProductRepository:

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def get_products(self) -> list[Product]:
        async with self.session_factory() as session:
            result = await session.execute(
                text("SELECT id, name, price, description FROM dbo.products")
            )
            return [Product(**row) for row in result.mappings()]
