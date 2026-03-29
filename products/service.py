from products.model import Product
from products.repository import ProductRepository
from features.service import FeatureService


class ProductService:

    def __init__(self, repo: ProductRepository, feature_service: FeatureService):
        self.repo = repo
        self.feature_service = feature_service

    async def get_products(self) -> list[Product]:
        products = await self.repo.get_products()
        features = await self.feature_service.get_features(product_id=2)

        return products
