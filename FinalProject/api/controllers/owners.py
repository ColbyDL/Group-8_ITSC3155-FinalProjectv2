from sqlalchemy.exc import NoResultFound
from sqlalchemy import func, and_, DECIMAL, Integer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends

# from fastapi import HTTPException, status, Response, Depends
# from ..models import orders as model
# from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, date
from ..models.orders import Orders
from ..models.dishesordered import DishesOrdered
from ..models.recipes import Recipes
from ..models.ingredients import Ingredients
from ..models.reviews import Reviews
from ..models.menu import Menu


def get_daily_revenue(db: Session, query_date: datetime) -> float:
    # Convert string query_date to datetime object for comparison, if necessary
    # Ensure query_date is passed as a datetime.date object
    query_date_start = datetime.combine(query_date, datetime.min.time())
    query_date_end = datetime.combine(query_date, datetime.max.time())

    total_revenue = (
        db.query(func.sum(Orders.totalPrice))
        .filter(
            and_(
                Orders.orderDate >= query_date_start,
                Orders.orderDate <= query_date_end,
            )
        )
        .scalar()
    )
    return total_revenue


def get_orders_by_date_range(db: Session, start_date: date, end_date: date):
    return (
        db.query(Orders)
        .filter(and_(Orders.orderDate >= start_date, Orders.orderDate <= end_date))
        .all()
    )


def get_orders_by_insufficient_ingredients(db: Session, order_id: int):
    try:
        amountavail = (
            db.query(Ingredients)
            .filter(
                and_(
                    DishesOrdered.orderId == order_id,
                    DishesOrdered.menuItem == Menu.menuItem,
                    Menu.menuItem == Recipes.menuItem,
                    Recipes.ingredientId == Ingredients.ingredientId,
                    Ingredients.amountAvailable < Recipes.amountRequired,
                )
            )
            .all()
        )

        return amountavail
    except NoResultFound:
        return "No order found with that ID."


def get_reviews_by_score(db: Session, score: int):
    return db.query(Reviews).filter(and_(Reviews.reviewScore == score)).all()
