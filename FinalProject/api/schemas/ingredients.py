# from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class IngredientsBase(BaseModel):
    amountAvailable: float
    ingredientName: str
    unit: str


class IngredientsCreate(IngredientsBase):
    pass


class IngredientsUpdate(BaseModel):
    amountAvailable: Optional[float] = None
    ingredientName: Optional[str] = None
    unit: Optional[str] = None


class Ingredients(IngredientsBase):
    ingredientId: int

    class ConfigDict:
        from_attributes = True
