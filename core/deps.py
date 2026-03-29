from fastapi import Depends

from features.repository import FeaturesRepository
from features.service import FeatureService
from products.repository import ProductRepository
from products.service import ProductService
from core.database import async_session


def get_product_repository():
    return ProductRepository(async_session)


def get_feature_repository():
    return FeaturesRepository(async_session)


def get_product_service(
    repo: ProductRepository = Depends(get_product_repository),
    feature_service: FeatureService = Depends(get_feature_repository),
):
    return ProductService(repo, feature_service)
