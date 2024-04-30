from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu as controller
from ..schemas import menu as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Menu"], prefix="/menu")


@router.post("/", response_model=schema.Menu)
def create(request: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Menu])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{menuItem}", response_model=schema.Menu)
def read_one(menuItem: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menuItem=menuItem)


@router.put("/{menuItem}", response_model=schema.Menu)
def update(menuItem: int, request: schema.MenuUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, menuItem=menuItem)


@router.delete("/{menuItem}")
def delete(menuItem: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menuItem=menuItem)
