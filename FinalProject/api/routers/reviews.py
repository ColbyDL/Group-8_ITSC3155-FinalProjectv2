from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas import reviews as schema
from ..dependencies.database import engine, get_db

router = APIRouter(tags=["Reviews"], prefix="/reviews")


@router.post("/", response_model=schema.Reviews)
def create(request: schema.ReviewsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Reviews])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{reviewId}", response_model=schema.Reviews)
def read_one(reviewId: int, db: Session = Depends(get_db)):
    return controller.read_one(db, reviewId=reviewId)


@router.put("/{reviewId}", response_model=schema.Reviews)
def update(reviewId: int, request: schema.ReviewsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, reviewId=reviewId)


@router.delete("/{reviewId}")
def delete(reviewId: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, reviewId=reviewId)
