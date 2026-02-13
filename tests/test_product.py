import pytest
from utilities.api_client import APIClient
from utilities.schema import products_schema
from jsonschema import validate

client = APIClient()

@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_products():
    response = client.get("/productsList")

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=products_schema)

    assert len(data["products"]) > 0
