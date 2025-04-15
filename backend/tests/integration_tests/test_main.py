import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={
        "name": "Test Item",
        "description": "A test item",
        "price": 99.99,
        "tax": 5.0
    })
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "price": 99.99}