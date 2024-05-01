from fastapi.testclient import TestClient
from ..controllers import recipes as controller
from ..main import app
import pytest
from ..models import recipes as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_recipes(db_session):
    # Create a sample menu
    recipes_data = {
        "menuItem": "1",
        "ingredientId": "1",
        "amountRequired": "1",
    }

    recipes_object = model.Recipes(**recipes_data)

    # Call the create function
    created_recipes = controller.create(db_session, recipes_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_recipes is not None
    assert created_recipes.menuItem == "1"  # type: ignore
    assert created_recipes.ingredientId == "1"  # type: ignore
    assert created_recipes.amountRequired == "1"  # type: ignore
