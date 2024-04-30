from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import users as controller
from ..schemas import menu as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/{foodCategory}", response_model=list[schema.Menu])
def read_all_categories(foodCategory: str, db: Session = Depends(get_db)):
    return controller.read_all_categories(db, foodCategory=foodCategory)


@router.get("/orderStatus/{trackingNumber}")
def read_order_status(trackingNumber: int, db: Session = Depends(get_db)):
    order = controller.get_order_status_by_tracking_number(db, trackingNumber)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {
        "tracking_number": trackingNumber,
        "order_status": order.orderStatus
    }

