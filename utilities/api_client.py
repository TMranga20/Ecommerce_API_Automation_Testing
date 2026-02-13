import requests
from utilities.config import BASE_URL

class APIClient:

    def get(self, endpoint, headers=None, params=None):
        return requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)

    def post(self, endpoint, headers=None, payload=None):
        return requests.post(f"{BASE_URL}{endpoint}", headers=headers, data=payload)

    def delete(self, endpoint, headers=None, payload=None):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=headers, data=payload)
