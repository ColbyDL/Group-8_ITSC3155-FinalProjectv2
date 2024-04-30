from sqlalchemy import func, and_, DECIMAL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends

from datetime import datetime


from ..models.orders import Orders


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
