import pytest
from utilities.api_client import APIClient

client = APIClient()

@pytest.mark.regression
def test_add_to_cart():
    payload = {
        "product_id": 1,
        "quantity": 2
    }

    response = client.post("/addToCart", payload=payload)

    assert response.status_code == 404
    assert "Page not found" in response.text


@pytest.mark.regression
def test_delete_cart():
    payload = {
        "product_id": 1
    }

    response = client.delete("/removeFromCart", payload=payload)

    assert response.status_code == 404
    assert "Page not found" in response.text
