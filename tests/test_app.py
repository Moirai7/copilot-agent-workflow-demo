import pytest
from app import app

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}

def test_temperature_accepts_valid_integer(client):
    r = client.post("/temperature", json={"value": 72})
    assert r.status_code == 200
    assert r.get_json() == {"accepted": True, "value": 72}

def test_temperature_accepts_valid_float(client):
    r = client.post("/temperature", json={"value": 72.5})
    assert r.status_code == 200
    assert r.get_json() == {"accepted": True, "value": 72.5}
