from src.api.handlers.health.health import healthz, readyz


def test_healthz_handler():
    response = healthz()
    assert response == {"message": "API is up and running!!"}

def test_readyz_handler():
    response = readyz()
    assert response == {"message": "API is up and running!!"}