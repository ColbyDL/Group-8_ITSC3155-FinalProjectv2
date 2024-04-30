from . import (
    customers,
    dishesordered,
    ingredients,
    menu,
    orders,
    promotions,
    recipes,
    reviews,
)

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    dishesordered.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
