import csv
from pathlib import Path

from app.schemas.market_data import DailyPriceRecord
from app.services.providers.base import MarketDataProvider

class CSVProvider(MarketDataProvider):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def get_daily_prices(self, symbol: str) -> list[DailyPriceRecord]:
        records = []

        with self.file_path.open(newline="") as file:
            reader = csv.DictReader(file)
            
            for row in reader: 
                if row["symbol"].upper() != symbol.upper():
                    continue

                records.append(
                    DailyPriceRecord(
                        symbol=row["symbol"].upper(),
                        date=row["date"],
                        open=row["open"],
                        high=row["high"],
                        low=row["low"],
                        close=row["close"],
                        volume=row["volume"]
                    )
                )

        return records