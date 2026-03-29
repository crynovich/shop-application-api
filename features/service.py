from features.model import Feature
from features.repository import FeaturesRepository


class FeatureService:
    def __init__(self, repo: FeaturesRepository):
        self.repo = repo

    async def get_features(self, product_id: int) -> list[Feature]:
        return await self.repo.get_features(product_id)
