from sqlalchemy import BOOLEAN, Column, ForeignKey, Integer, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from ..dependencies.database import Base


class Orders(Base):
    __tablename__ = "orders"

    trackingNumber = Column(Integer, primary_key=True, index=True, autoincrement=True)
    orderDate = Column(DATETIME, nullable=False, default=datetime.now)
    customerId = Column(Integer, ForeignKey("customers.customerId"))
    orderStatus = Column(BOOLEAN, unique=False, default=False)
    promotionCode = Column(Integer, ForeignKey("promotions.promotionCode"))
    transactionStatus = Column(BOOLEAN, unique=False, default=False)
    totalPrice = Column(DECIMAL(4, 2), nullable=False, server_default="0.0")
    takeOut = Column(BOOLEAN, unique=False, default=False)

    """
    @hybrid_property
    def totalPrice(self):
        return (
            select(func.sum(Menu.price))
            .where(DishesOrdered.trackingNumber == Orders.trackingNumber)
            .where(Menu.menuItem == DishesOrdered.menuItem)
            .label("totalPrice")
        )
    """

    customers = relationship("Customers", backref="orders")
    promotions = relationship("Promotions", backref="orders")
