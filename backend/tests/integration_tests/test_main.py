import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from main import app
from datetime import datetime, timezone

client = TestClient(app)

def test_create_item():
    curr_date = datetime.now(timezone.utc).isoformat()
    response = client.post("/app/messages", json={
        "name": "Test User",
        "message": "Hello from test!",
        "subject": "Testing",
        "date": curr_date
    })
    assert response.status_code == 200
    response_data = response.json()

    assert response_data["name"] == "Test User"
    assert response_data["message"] == "Hello from test!"
    assert response_data["subject"] == "Testing"