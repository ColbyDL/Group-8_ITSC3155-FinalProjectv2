from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class DishesOrdered(Base):
    __tablename__ = "dishesOrdered"

    orderId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trackingNumber = Column(Integer, ForeignKey("orders.trackingNumber"))
    menuItem = Column(Integer, ForeignKey("menu.menuItem"))

    menu = relationship("Menu", backref="dishesOrdered")
    orders = relationship("Orders", backref="dishesOrdered")
