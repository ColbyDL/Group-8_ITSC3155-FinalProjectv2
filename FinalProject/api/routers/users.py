from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import users as controller
from ..schemas import menu as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/{foodCategory}", response_model=list[schema.Menu])
def read_all_categories(foodCategory: str, db: Session = Depends(get_db)):
    if foodCategory:
        return controller.read_all_categories(db=db, foodCategory=foodCategory)
    return controller.read_all_categories(db=db)
