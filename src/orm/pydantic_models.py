from typing import Optional
from pydantic import BaseModel, NonNegativeInt


class ProductPayload(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    category: Optional[str] = None
    unit_price: Optional[NonNegativeInt] = None
    inventory: Optional[NonNegativeInt] = None
    sizes: list[str] = []
    colors: list[str] = []
