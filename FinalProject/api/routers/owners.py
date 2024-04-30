from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import owners as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import datetime, date

router = APIRouter(tags=["Owners"], prefix="/owners")


@router.get("/revenue/{query_date}", response_model=dict)
def read_daily_revenue(query_date: datetime, db: Session = Depends(get_db)):
    revenue = controller.get_daily_revenue(db, query_date)
    if revenue is None:
        raise HTTPException(status_code=404, detail="Revenue data not available for this date")
    return {"date": query_date, "revenue": float(revenue)}


@router.get("/orders/{start_date}/{end_date}")
def read_orders_by_date_range(start_date: date, end_date: date, db: Session = Depends(get_db)):
    orders = controller.get_orders_by_date_range(db, start_date, end_date)
    if not orders:
        raise HTTPException(status_code=404, detail="No order found for this date range")
    return orders

@router.get("/reviews/{score}")
def read_reviews_by_score(score: int, db: Session = Depends(get_db)):
    reviews = controller.get_reviews_by_score(db, score)
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found with this score")
    return reviews
