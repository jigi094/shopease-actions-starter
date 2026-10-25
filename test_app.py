import os
import pytest
from app import app, PRICES


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_price_known_item(client):
    r = client.get("/price/laptop")
    assert r.get_json()["price"] == PRICES["laptop"]


def test_price_unknown_item(client):
