from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_one_buyer():
    response = client.post("/{buyer_id}")
    
    assert response.status_code == 200
    assert response.json()