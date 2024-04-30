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


def load_routes(app):
    app.include_router(customers.router)
    app.include_router(dishesordered.router)
    app.include_router(ingredients.router)
    app.include_router(menu.router)
    app.include_router(orders.router)
    app.include_router(promotions.router)
    app.include_router(recipes.router)
    app.include_router(reviews.router)
