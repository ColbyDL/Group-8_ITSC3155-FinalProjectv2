from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post("/", response_model=schema.Orders)
def create(request: schema.OrdersCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Orders])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{trackingNumber}", response_model=schema.Orders)
def read_one(trackingNumber: int, db: Session = Depends(get_db)):
    return controller.read_one(db, trackingNumber=trackingNumber)


@router.put("/{trackingNumber}", response_model=schema.Orders)
def update(
    trackingNumber: int, request: schema.OrdersUpdate, db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, trackingNumber=trackingNumber)


@router.delete("/{trackingNumber}")
def delete(trackingNumber: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, trackingNumber=trackingNumber)
