from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import ingredients as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Ingredients(
        amountAvailable=request.amountAvailable,
        ingredientName=request.ingredientName,
        unit=request.unit,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Ingredients).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, ingredientId):
    try:
        item = (
            db.query(model.Ingredients)
            .filter(model.Ingredients.ingredientId == ingredientId)
            .first()
        )
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!"
            )
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, ingredientId, request):
    try:
        item = db.query(model.Ingredients).filter(
            model.Ingredients.ingredientId == ingredientId
        )
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!"
            )
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, ingredientId):
    try:
        item = db.query(model.Ingredients).filter(
            model.Ingredients.ingredientId == ingredientId
        )
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!"
            )
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
