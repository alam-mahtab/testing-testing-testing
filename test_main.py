from fastapi.testclient import TestClient
from api.main import app

Client = TestClient(app)

def test_active():
    response = Client.on_event("startup")
    assert response.status_code == 200

def test_inactive():
    response = Client.on_event("shutdown")
    assert response.status_code == 200

def test_read():
    response = Client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World"}