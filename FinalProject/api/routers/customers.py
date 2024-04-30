from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Customers"], prefix="/customers")


@router.post("/", response_model=schema.Customers)
def create(request: schema.CustomersCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Customers])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{customerId}", response_model=schema.Customers)
def read_one(customerId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, customerId=customerId)


@router.put("/{customerId}", response_model=schema.Customers)
def update(
    customerId: int, request: schema.CustomersUpdate, db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, customerId=customerId)


@router.delete("/{customerId}")
def delete(customerId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, customerId=customerId)
