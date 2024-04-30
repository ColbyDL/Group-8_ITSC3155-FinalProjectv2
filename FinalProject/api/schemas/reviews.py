# from datetime import datetime
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .menu import Menu


class ReviewsBase(BaseModel):
    reviewText: str
    reviewScore: int


class ReviewsCreate(ReviewsBase):
    menuItem: int


class ReviewsUpdate(BaseModel):
    reviewText: Optional[str] = None
    reviewScore: Optional[int] = None
    menuItem: Optional[int] = None


class Reviews(ReviewsBase):
    reviewId: int
    reviewDate: datetime
    menu: Menu

    class ConfigDict:
        from_attributes = True
