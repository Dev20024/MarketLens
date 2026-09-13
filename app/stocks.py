from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from database.repositories import get_all_stocks

stocks_router = APIRouter()

@stocks_router.get("/stocks")
async def get_stocks(db: Session = Depends(get_db)):
    return get_all_stocks(db)