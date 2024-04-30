# from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .menu import Menu
from .ingredients import Ingredients


class RecipesBase(BaseModel):
    amountRequired: float


class RecipesCreate(RecipesBase):
    menuItem: int
    ingredientId: int


class RecipesUpdate(BaseModel):
    amountRequired: Optional[float] = None
    menuItem: Optional[int] = None
    ingredientId: Optional[int] = None


class Recipes(RecipesBase):
    recipeId: int
    menu: Menu
    ingredients: Ingredients

    class ConfigDict:
        from_attributes = True
