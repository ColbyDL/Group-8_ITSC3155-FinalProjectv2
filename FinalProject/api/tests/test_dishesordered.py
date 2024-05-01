from fastapi.testclient import TestClient
from ..controllers import dishesordered as controller
from ..main import app
import pytest
from ..models import dishesordered as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_dishesordered(db_session):
    # Create a sample menu
    dishesordered_data = {
        "trackingNumber": "1",
        "menuItem": "1",
    }

    dishesordered_object = model.DishesOrdered(**dishesordered_data)

    # Call the create function
    created_dishesordered = controller.create(db_session, dishesordered_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_dishesordered is not None
    assert created_dishesordered.trackingNumber == "1"  # type: ignore
    assert created_dishesordered.menuItem == "1"  # type: ignore
