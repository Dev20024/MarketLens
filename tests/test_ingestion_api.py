import pytest

from fastapi.testclient import TestClient

from app.database.models import Stock
from app.main import app

client = TestClient(app)

def test_ingest_symbol(db_session):
    stock = Stock(
        symbol="AAPL",
        company_name="Apple Inc.",
        exchange="NASDAQ",
        sector="Technology",
    )

    db_session.add(stock)
    db_session.commit()
    

    response = client.post("/ingestion/AAPL")

    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
    assert response.json()["inserted_count"] == 2


def test_ingest_missing_symbol():
    response = client.post("/ingestion/DOESNOTEXIT")

    assert response.status_code == 404


