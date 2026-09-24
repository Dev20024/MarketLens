from app.database.models import Stock
from app.services.ingestion import ingest_daily_prices
from app.services.providers.csv_provider import CSVProvider
from tests.conftest import TestingSessionLocal



def test_ingest_daily_prices():
    db = TestingSessionLocal()

    stock = Stock(
        symbol="AAPL",
        company_name="Apple Inc.",
        exchange="NASDAQ",
        sector="Technology",
    )

    db.add(stock)
    db.commit()

    provider = CSVProvider("data/sample_prices.csv")

    inserted = ingest_daily_prices(db, provider, "AAPL")

    assert inserted == 2

    db.close()

def test_ingestion_is_idempotent():
    db = TestingSessionLocal()

    stock = Stock(
        symbol="AAPL",
        company_name="Apple Inc.",
        exchange="NASDAQ",
        sector="Technology",
    )

    db.add(stock)
    db.commit()

    provider = CSVProvider("data/sample_prices.csv")

    first_run = ingest_daily_prices(db, provider, "AAPL")
    second_run = ingest_daily_prices(db, provider, "AAPL")

    assert first_run == 2
    assert second_run == 0

    db.close()
