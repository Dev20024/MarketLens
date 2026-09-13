from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import Stock


def get_all_stocks(db: Session):
    statement = select(Stock)
    result = db.execute(statement)

    return result.scalars().all()

def get_stock_by_symbol(db: Session, symbol: str):
    statement = select(Stock).where(Stock.symbol == symbol)
    result = db.execute(statement)

    return result.scalar_one_ornone()