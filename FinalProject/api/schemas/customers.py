# from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomersBase(BaseModel):
    name: str
    email: str
    phoneNumber: str
    address: str
    cardInfo: str
    cardType: str


class CustomersCreate(CustomersBase):
    pass


class CustomersUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None
    address: Optional[str] = None
    cardInfo: Optional[str] = None
    cardType: Optional[str] = None


class Customers(CustomersBase):
    customerId: int

    class ConfigDict:
        from_attributes = True
