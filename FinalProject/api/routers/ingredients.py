from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import ingredients as controller
from ..schemas import ingredients as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Ingredients"], prefix="/ingredients")


@router.post("/", response_model=schema.Ingredients)
def create(request: schema.IngredientsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Ingredients])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{ingredientId}", response_model=schema.Ingredients)
def read_one(ingredientId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, ingredientId=ingredientId)


@router.put("/{ingredientId}", response_model=schema.Ingredients)
def update(
    ingredientId: int, request: schema.IngredientsUpdate, db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, ingredientId=ingredientId)


@router.delete("/{ingredientId}")
def delete(ingredientId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, ingredientId=ingredientId)
