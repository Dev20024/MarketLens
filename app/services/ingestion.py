from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.repositories import get_stock_by_symbol
from app.database.models import DailyPrice
from app.services.providers.base import MarketDataProvider


def ingest_daily_prices(db: Session, provider: MarketDataProvider, symbol: str) -> int:
    stock = get_stock_by_symbol(db, symbol)

    if stock is None:
        raise ValueError(f"Stock '{symbol}' does not exist")

    records = provider.get_daily_prices(symbol)


    inserted_count = 0
    for record in records:
        statement = select(DailyPrice).where(
            DailyPrice.stock_id == stock.id,
            DailyPrice.date == record.date,
        )

        existing = db.execute(statement).scalar_one_or_none()

        if existing is not None:
            continue
        
        
        daily_price = DailyPrice(
            stock_id=stock.id,
            date=record.date,
            open=record.open,
            high=record.high,
            low=record.low,
            close=record.close,
            volume=record.volume,
        )

        db.add(daily_price)
        inserted_count += 1

    db.commit()
    return inserted_count
    