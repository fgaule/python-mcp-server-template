import pytest
from starlette.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.mark.integration
def test_healtz_endpoint():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running!!"}

@pytest.mark.integration
def test_readyz_endpoint():
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running!!"}
