import pytest
from app import create_app
from app.utils import validate_title

@pytest.fixture
def client():
    return create_app().test_client()

def test_validate_title():
    assert validate_title("Belajar DevSecOps")
    assert not validate_title("   ")
    assert not validate_title(123)

def test_create_and_list(client):
    res = client.post("/tasks", json={"title": "Tugas 1"})
    assert res.status_code == 201
    assert len(client.get("/tasks").get_json()) == 1

def test_invalid_title(client):
    assert client.post("/tasks", json={"title": ""}).status_code == 400

def test_complete_and_delete(client):
    client.post("/tasks", json={"title": "A"})
    assert client.put("/tasks/1/complete").get_json()["done"] is True
    assert client.delete("/tasks/1").status_code == 204
    assert client.delete("/tasks/1").status_code == 404