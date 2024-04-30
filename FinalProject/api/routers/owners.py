from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import owners as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import datetime


router = APIRouter(tags=["Owners"], prefix="/owners")


@router.get("/revenue/{query_date}", response_model=dict)
def read_daily_revenue(query_date: datetime, db: Session = Depends(get_db)):
    revenue = controller.get_daily_revenue(db, query_date)
    if revenue is None:
        raise HTTPException(
            status_code=404, detail="Revenue data not available for this date"
        )
    return {"date": query_date, "revenue": float(revenue)}
