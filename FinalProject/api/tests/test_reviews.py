from fastapi.testclient import TestClient
from ..controllers import reviews as controller
from ..main import app
import pytest
from ..models import reviews as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_reviews(db_session):
    # Create a sample menu
    reviews_data = {
        "reviewText": "great",
        "reviewScore": "9",
        "menuItem": "1",
    }

    reviews_object = model.Reviews(**reviews_data)

    # Call the create function
    created_reviews = controller.create(db_session, reviews_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_reviews is not None
    assert created_reviews.reviewText == "great"  # type: ignore
    assert created_reviews.reviewScore == "9"  # type: ignore
    assert created_reviews.menuItem == "1"  # type: ignore
