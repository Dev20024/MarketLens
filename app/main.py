from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "name": "MarketLens",
        "status": "running"
    }

@app.get("/about")
async def about():
    return {
        "project": "MarketLens",
        "description": "Market data analytics platform"
    }