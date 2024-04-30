from sqlalchemy import FLOAT, Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Ingredients(Base):
    __tablename__ = "ingredients"

    ingredientId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredientName = Column(String(100), unique=True, nullable=False)
    amountAvailable = Column(DECIMAL(4, 2), nullable=False, server_default="0.0")
    unit = Column(String(10), nullable=False, server_default="unit")
