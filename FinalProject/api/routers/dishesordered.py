from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import dishesordered as controller
from ..schemas import dishesordered as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Dishes Ordered"], prefix="/dishesordered")


@router.post("/", response_model=schema.DishesOrdered)
def create(request: schema.DishesOrderedCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.DishesOrdered])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{orderId}", response_model=schema.DishesOrdered)
def read_one(orderId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, orderId=orderId)


@router.put("/{orderId}", response_model=schema.DishesOrdered)
def update(
    orderId: int, request: schema.DishesOrderedUpdate, db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, orderId=orderId)


@router.delete("/{orderId}")
def delete(orderId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, orderId=orderId)
