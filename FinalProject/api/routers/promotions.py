from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Promotions"], prefix="/promotions")


@router.post("/", response_model=schema.Promotions)
def create(request: schema.PromotionsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Promotions])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{promotionCode}", response_model=schema.Promotions)
def read_one(promotionCode: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promotionCode=promotionCode)


@router.put("/{promotionCode}", response_model=schema.Promotions)
def update(
    promotionCode: int, request: schema.PromotionsUpdate, db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, promotionCode=promotionCode)


@router.delete("/{promotionCode}")
def delete(promotionCode: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promotionCode=promotionCode)
