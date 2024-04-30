from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Recipes"], prefix="/recipes")


@router.post("/", response_model=schema.Recipes)
def create(request: schema.RecipesCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Recipes])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{recipeId}", response_model=schema.Recipes)
def read_one(recipeId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, recipeId=recipeId)


@router.put("/{recipeId}", response_model=schema.Recipes)
def update(recipeId: int, request: schema.RecipesUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, recipeId=recipeId)


@router.delete("/{recipeId}")
def delete(recipeId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, recipeId=recipeId)
