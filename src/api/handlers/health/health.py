"""Module containing health check handlers."""

def healthz():
    return {"message": "API is up and running!!"}

def readyz():
    return {"message": "API is up and running!!"}
