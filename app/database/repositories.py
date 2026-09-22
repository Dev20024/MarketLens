from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.models import Stock

from app.schemas.stocks import StockCreate


def get_all_stocks(db: Session):
    statement = select(Stock)
    result = db.execute(statement)

    return result.scalars().all()

def get_stock_by_symbol(db: Session, symbol: str):
    statement = select(Stock).where(Stock.symbol == symbol)
    result = db.execute(statement)

    return result.scalar_one_ornone()

def create_stock(db: Session, stock_data: StockCreate):
    stock = Stock(
        symbol=stock_data.symbol,
        company_name=stock_data.company_name,
        exchange=stock_data.exchange,
        sector=stock_data.sector,
    )
    try:
        db.add(stock)
        db.commit()
        db.refresh(stock)
        return stock
    except IntegrityError:
        db.rollback()
        raise