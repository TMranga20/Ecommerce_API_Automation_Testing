from utilities.api_client import APIClient
from utilities.config import EMAIL, PASSWORD
from utilities.schema import login_schema
from jsonschema import validate


client = APIClient()

def ensure_valid_user(email, password):
    verify_response = client.post("/verifyLogin", payload={"email": email, "password": password})
    verify_data = verify_response.json()

    if verify_data.get("responseCode") == 200:
        return

    create_payload = {
        "name": "API Test User",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "January",
        "birth_year": "2000",
        "firstname": "API",
        "lastname": "User",
        "company": "Automation",
        "address1": "123 Test Street",
        "address2": "Suite 1",
        "country": "India",
        "zipcode": "500001",
        "state": "TS",
        "city": "Hyderabad",
        "mobile_number": "9999999999"
    }

    create_response = client.post("/createAccount", payload=create_payload)
    assert create_response.status_code == 200
    create_data = create_response.json()

    if create_data.get("responseCode") == 201:
        return

    if create_data.get("responseCode") == 400:
        delete_response = client.delete("/deleteAccount", payload={"email": email, "password": password})
        assert delete_response.status_code == 200
        delete_data = delete_response.json()
        assert delete_data.get("responseCode") == 200, f"Unable to reset existing account: {delete_data}"

        recreate_response = client.post("/createAccount", payload=create_payload)
        assert recreate_response.status_code == 200
        recreate_data = recreate_response.json()
        assert recreate_data.get("responseCode") == 201, f"Unable to recreate account: {recreate_data}"
        return

    assert False, f"Unexpected createAccount response: {create_data}"

def test_valid_login():
    ensure_valid_user(EMAIL, PASSWORD)

    payload = {
        "email": EMAIL,
        "password": PASSWORD
    }

    response = client.post("/verifyLogin", payload=payload)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=login_schema)

    assert data["responseCode"] == 200
    assert "User exists" in data["message"]


def test_invalid_login():
    payload = {
        "email": "wrong@yopmail.com",
        "password": "wrong123"
    }

    response = client.post("/verifyLogin", payload=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 404
    assert "User not found" in data["message"]
    
