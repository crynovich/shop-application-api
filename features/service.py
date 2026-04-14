from features.model import Feature
from features.repository import FeaturesRepository
from core.logging import get_logger

logger = get_logger(__name__)


class FeatureService:
    def __init__(self, repo: FeaturesRepository):
        self.repo = repo

    async def get_features(self, product_id: int) -> list[Feature]:
        logger.debug("Fetching features for product_id=%d", product_id)
        return await self.repo.get_features(product_id)
