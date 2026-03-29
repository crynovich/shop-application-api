from sqlalchemy import text

from features.model import Feature


class FeaturesRepository:

    def __init__(self, session_factory):
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
            return [Feature(**row._mapping) for row in result]
