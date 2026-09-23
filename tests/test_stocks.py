from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_stocks():
    response = client.get("/stocks")
    assert response.status_code == 200

def test_create_stock():
    response = client.post(
        "/stocks",
        json={
            "symbol": "AAPL",
            "company_name": "Apple Inc.",
            "exchange": "NASDAQ",
            "sector": "Technology"
        },
    )

    assert response.status_code == 201
    assert response.json()["symbol"] == "AAPL"

def test_get_stock_by_symbol():
    client.post(
        "/stocks",
        json={
            "symbol": "AAPL",
            "company_name": "Apple Inc.",
            "exchange": "NASDAQ",
            "sector": "Technology",
        },
    )

    response = client.get("/stocks/AAPL")

    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"

def test_get_missing_stock():
    response = client.get("/stocks/DOESNOTEXIT")

    assert response.status_code == 404

def test_duplicate_stock():
    stock_data = {
        "symbol": "AAPL",
        "company_name": "Apple Inc.",
        "exchange": "NASDAQ",
        "sector": "Technology",
    }
    
    first_response = client.post("/stocks", json=stock_data)
    second_response = client.post("/stocks", json=stock_data)

    assert first_response.status_code == 201
    assert second_response.status_code == 409