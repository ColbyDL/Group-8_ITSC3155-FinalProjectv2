from fastapi.testclient import TestClient
from ..controllers import promotions as controller
from ..main import app
import pytest
from ..models import promotions as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotions(db_session):
    # Create a sample menu
    promotions_data = {
        "promotionCode": "1",
        "discount": "5",
        "promotionExpiration": "3000-05-01",
    }

    promotions_object = model.Promotions(**promotions_data)

    # Call the create function
    created_promotions = controller.create(db_session, promotions_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_promotions is not None
    assert created_promotions.promotionCode == "1"  # type: ignore
    assert created_promotions.discount == "5"  # type: ignore
    assert created_promotions.promotionExpiration == "3000-05-01"  # type: ignore
