from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends

from api.controllers import customers
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError

from ..models.orders import Orders
from ..models import customers as user


def create_guest(db: Session):
    new_guest = user.Customers(
        name="guest",
        email="guest",
        phoneNumber="guest",
        address="guest",
        cardInfo="1234",
        cardType="1234",
    )

    try:
        db.add(new_guest)
        db.commit()
        db.refresh(new_guest)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_guest


def read_all_categories(db: Session, foodCategory: str):
    try:
        result = (
            db.query(model.Menu).filter(model.Menu.foodCategory == foodCategory).all()
        )
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def get_order_status_by_tracking_number(db: Session, trackingNumber: int):
    order = (
        db.query(Orders).filter(and_(Orders.trackingNumber == trackingNumber)).first()
    )
    return order
