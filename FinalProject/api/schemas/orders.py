from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .customers import Customers
from .promotions import Promotions


class OrdersBase(BaseModel):
    orderStatus: bool
    transactionStatus: bool
    totalPrice: float


class OrdersCreate(OrdersBase):
    customerId: int
    promotionCode: int


class OrdersUpdate(BaseModel):
    orderStatus: Optional[bool] = None
    transactionStatus: Optional[bool] = None
    customerId: Optional[int] = None
    promotionCode: Optional[int] = None
    totalPrice: Optional[float] = None


class Orders(OrdersBase):
    trackingNumber: int
    orderDate: datetime
    customers: Customers
    promotions: Promotions

    class ConfigDict:
        from_attributes = True
