from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customers(Base):
    __tablename__ = "customers"

    customerId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    phoneNumber = Column(String(100), unique=True, nullable=True)
    address = Column(String(100), unique=True, nullable=True)
    cardInfo = Column(String(100), unique=True, nullable=True)
    cardType = Column(String(100), unique=True, nullable=True)
