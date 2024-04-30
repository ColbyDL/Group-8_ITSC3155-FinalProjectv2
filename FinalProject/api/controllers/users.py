from sqlalchemy import and_, func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends

from api.controllers import customers
from api.models.dishesordered import DishesOrdered
from api.models.promotions import Promotions
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


def finished_ordering(
    db: Session, finished: bool, trackingNumber: int, promotionCode: int
):
    if finished:
        total_revenue = (
            db.query(func.sum(model.Menu.price))
            .filter(
                and_(
                    DishesOrdered.trackingNumber == trackingNumber,
                    DishesOrdered.menuItem == model.Menu.menuItem,
                )
            )
            .scalar()
        )
        cust = db.query(Orders).where(Orders.trackingNumber == trackingNumber).one()
        promo = (
            db.query(Promotions.discount)
            .filter(and_(Promotions.promotionCode == promotionCode))
            .scalar()
        )
        total_revenue -= promo
        cust.totalPrice = total_revenue

        db.commit()

        return total_revenue

    else:
        return


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
