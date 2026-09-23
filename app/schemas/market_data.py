from pydantic import BaseModel
from datetime  import date

class DailyPriceRecord(BaseModel):
    symbol: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    