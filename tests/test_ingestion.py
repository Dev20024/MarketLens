from pydantic import ValidationError

from app.database.models import Stock
from app.services.ingestion import ingest_daily_prices
from app.services.providers.csv_provider import CSVProvider
from tests.conftest import TestingSessionLocal
import pytest



def test_ingest_daily_prices(db_session):
    db_session = TestingSessionLocal()

    stock = Stock(
        symbol="AAPL",
        company_name="Apple Inc.",
        exchange="NASDAQ",
        sector="Technology",
    )

    db_session.add(stock)
    db_session.commit()

    provider = CSVProvider("data/sample_prices.csv")

    inserted = ingest_daily_prices(db_session, provider, "AAPL")

    assert inserted == 2

    db_session.close()

def test_ingestion_is_idempotent(db_session):
    db_session

    stock = Stock(
        symbol="AAPL",
        company_name="Apple Inc.",
        exchange="NASDAQ",
        sector="Technology",
    )

    db_session.add(stock)
    db_session.commit()

    provider = CSVProvider("data/sample_prices.csv")

    first_run = ingest_daily_prices(db_session, provider, "AAPL")
    second_run = ingest_daily_prices(db_session, provider, "AAPL")

    assert first_run == 2
    assert second_run == 0

    db_session.close()

def test_ingetion_missing_stock(db_session):
    provider = CSVProvider("data/bad_prices.csv")

    with pytest.raises(ValidationError):
        provider.get_daily_prices("AAPL")
