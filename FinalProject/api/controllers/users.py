from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError


def read_all_categories(db: Session, foodCategory: str):
    try:
        result = (
            db.query(model.Menu).filter(model.Menu.foodCategory == foodCategory).all()
        )
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result
