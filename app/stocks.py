from fastapi import APIRouter

stocks_router = APIRouter()

@stocks_router.get("/stocks")
async def get_stocks():
    return {
        "message": "Welcome to MarketLens Stocks API"
    }