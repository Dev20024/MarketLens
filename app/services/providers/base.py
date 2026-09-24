from abc import ABC, abstractmethod

from app.schemas.market_data import DailyPriceRecord

class MarketDataProvider(ABC):

    @abstractmethod
    def get_daily_prices(self, symbol: str) -> list[DailyPriceRecord]:
        pass