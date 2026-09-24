from app.services.providers.csv_provider import CSVProvider
from datetime import date

def test_csv_provider_returns_appl_rows():
    provider = CSVProvider("data/sample_prices.csv")

    records = provider.get_daily_prices("AAPL")

    assert len(records) == 2
    assert records[0].symbol == "AAPL"

def test_csv_provider_converts_types():
    provider = CSVProvider("data/sample_prices.csv")

    record = provider.get_daily_prices("AAPL")[0]

    assert isinstance(record.date, date)
    assert isinstance(record.open, float)
    assert isinstance(record.volume, int)
