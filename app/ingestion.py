from fastapi import APIRouter, Depends, HTTPException, status, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.connection import get_db
from app.services.ingestion import ingest_daily_prices
from app.services.providers.csv_provider import CSVProvider


ingestion_router = APIRouter()

@ingestion_router.post("/ingestion/{symbol}")
async def ingest_symbol(symbol: str, db: Session = Depends(get_db)):
    provider = CSVProvider("data/sample_prices.csv")

    try:
        inserted_count = ingest_daily_prices(
            db,
            provider,
            symbol,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )

    return {
        "symbol": symbol,
        "inserted_count": inserted_count
    }