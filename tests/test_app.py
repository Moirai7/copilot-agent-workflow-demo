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

@pytest.mark.parametrize("value", [72, 72.5, -100, 200])
def test_temperature_accepts_valid_values(client, value):
    r = client.post("/temperature", json={"value": value})
    assert r.status_code == 200
    assert r.get_json() == {"accepted": True, "value": value}

def test_temperature_rejects_missing_value(client):
    r = client.post("/temperature", json={})
    assert r.status_code == 400

@pytest.mark.parametrize("value", ["hot", None, True])
def test_temperature_rejects_non_numeric_value(client, value):
    r = client.post("/temperature", json={"value": value})
    assert r.status_code == 400

@pytest.mark.parametrize("value", [-101, 201])
def test_temperature_rejects_out_of_range_value(client, value):
    r = client.post("/temperature", json={"value": value})
    assert r.status_code == 400
