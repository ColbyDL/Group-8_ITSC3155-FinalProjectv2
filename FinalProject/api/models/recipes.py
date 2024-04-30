from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Recipes(Base):
    __tablename__ = "recipes"

    recipeId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menuItem = Column(Integer, ForeignKey("menu.menuItem"))
    ingredientId = Column(Integer, ForeignKey("ingredients.ingredientId"))
    amountRequired = Column(Integer, nullable=False, server_default="0.0")

    menu = relationship("Menu", backref="recipes")
    ingredients = relationship("Ingredients", backref="recipes")
