# from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .orders import Orders
from .menu import Menu


class DishesOrderedBase(BaseModel):
    pass


class DishesOrderedCreate(DishesOrderedBase):
    trackingNumber: int
    menuItem: int


class DishesOrderedUpdate(BaseModel):
    trackingNumber: Optional[int] = None
    menuItem: Optional[int] = None


class DishesOrdered(DishesOrderedBase):
    orderId: int
    orders: Orders
    menu: Menu

    class ConfigDict:
        from_attributes = True
