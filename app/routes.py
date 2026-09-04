from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def root():
    return {
        "name": "MarketLens",
        "status": "running"
    }

@router.get("/about")
async def about():
    return {
        "project": "MarketLens",
        "description": "Market data analytics platform"
    }

@router.get("/hello")
async def hello():
    return {
        "message": "Hello from MarketLens"

    }