from pydantic import BaseModel, ConfigDict
from datetime import datetime

class StockResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    symbol: str
    company_name: str
    exchange: str
    sector: str | None
    created_at: datetime

class StockCreate(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    sector: str | None = None