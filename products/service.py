from products.repository import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_products(self):
        return self.repo.get_products()
