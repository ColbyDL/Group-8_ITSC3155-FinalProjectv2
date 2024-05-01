from fastapi.testclient import TestClient
from ..controllers import ingredients as controller
from ..main import app
import pytest
from ..models import ingredients as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_ingredients(db_session):
    # Create a sample menu
    ingredients_data = {
        "amountAvailable": "20",
        "ingredientName": "ham",
        "unit": "slice",
    }

    ingredients_object = model.Ingredients(**ingredients_data)

    # Call the create function
    created_ingredients = controller.create(db_session, ingredients_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_ingredients is not None
    assert created_ingredients.amountAvailable == "20"  # type: ignore
    assert created_ingredients.ingredientName == "ham"  # type: ignore
    assert created_ingredients.unit == "slice"  # type: ignore
