from fastapi import APIRouter, Depends, HTTPException, status, FastAPI
from sqlalchemy.orm import Session

from database.connection import get_db
from database.repositories import get_all_stocks
from database.repositories import get_stock_by_symbol
from database.repositories import create_stock


from schemas.stocks import StockResponse, StockCreate

stocks_router = APIRouter()

@stocks_router.get("/stocks", response_model=list[StockResponse])
async def get_stocks(db: Session = Depends(get_db)):
    return get_all_stocks(db)

@stocks_router.get("/stocks/{symbol}", response_model=StockResponse)
async def get_stock(symbol: str, db: Session = Depends(get_db)):
    response = get_stock_by_symbol(db, symbol)

    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="symbol couldn't be found"
        )
    
    return response

@stocks_router.post("/stocks", response_model=StockResponse, status_code=status.HTTP_201_CREATED)
async def add_stock(
    stock_data: StockCreate,
    db: Session = Depends(get_db),
):
    return create_stock(db, stock_data)