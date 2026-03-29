from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from features.model import Feature


class FeaturesRepository:

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def get_features(self, product_id: int) -> list[Feature]:
        async with self.session_factory() as session:
            result = await session.execute(
                text(
                    "select f.id, f.name from dbo.features f "
                    "left join dbo.products_features pf on pf.feature_id = f.id "
                    "where pf.product_id = :product_id"
                ),
                {"product_id": product_id},
            )
            return [Feature(**row) for row in result.mappings()]
