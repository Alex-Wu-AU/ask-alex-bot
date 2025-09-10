"""Stage 1 basic test for the placeholder /ask endpoint.

Run after adding pytest to requirements (Prompt 5).
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ask_placeholder():
    payload = {"question": "ping"}
    response = client.post("/ask", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == "Hello, Ask Alex is working"
    assert data.get("source_type") == "placeholder"