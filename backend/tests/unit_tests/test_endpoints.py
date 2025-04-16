from main import app
from datetime import datetime, timezone
from fastapi.testclient import TestClient


client = TestClient(app)

def test_root():
    response = client.get("/app/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_post_prompt():
    curr_date = datetime.now(timezone.utc).isoformat()
    test_prompt = {
        "name": "Test User",
        "message": "Hello from test!",
        "subject": "Testing",
        "date": curr_date
    }
    response = client.post("/app/messages",json=test_prompt)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["message"] == "Hello from test!"
    assert data["subject"] == "Testing"