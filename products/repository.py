from sqlalchemy import text

from products.model import Product


class ProductRepository:
    def __init__(self, engine):
        self.engine = engine

    def get_products(self) -> list[Product]:
        with self.engine.connect() as conn:
            result = conn.execute(
                text(
                    "SELECT id, name, price, description FROM dbo.products WHERE price > :price"
                ),
                {"price": 2},
            )
            return [Product(**row._mapping) for row in result]
