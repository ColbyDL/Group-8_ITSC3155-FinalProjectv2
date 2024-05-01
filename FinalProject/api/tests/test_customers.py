from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import customers as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customers(db_session):
    # Create a sample menu
    customers_data = {
        "name": "jimmy",
        "email": "jimmy@",
        "phoneNumber": "1234",
        "address": "1234 drive",
        "cardInfo": "1234",
        "cardType": "visa",
    }

    customers_object = model.Customers(**customers_data)

    # Call the create function
    created_customers = controller.create(db_session, customers_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_customers is not None
    assert created_customers.name == "jimmy"  # type: ignore
    assert created_customers.email == "jimmy@"  # type: ignore
    assert created_customers.phoneNumber == "1234"  # type: ignore
    assert created_customers.address == "1234 drive"  # type: ignore
    assert created_customers.cardInfo == "1234"  # type: ignore
    assert created_customers.cardType == "visa"  # type: ignore
