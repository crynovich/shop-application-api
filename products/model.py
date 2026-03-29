from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    features: Optional[list[str]] = None
    # specifications
