from core.database import async_session
from features.repository import FeaturesRepository
from features.service import FeatureService
from products.model import Product
from products.repository import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    async def get_products(self) -> list[Product]:
        repo = FeaturesRepository(session_factory=async_session)
        feature_service = FeatureService(repo)
        products = await self.repo.get_products()
        features = await feature_service.get_features(product_id=2)

        # for product in products:
        #     product.features =

        return await self.repo.get_products()
