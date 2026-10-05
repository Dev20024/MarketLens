from fastapi import FastAPI

# import API routers
from app.routes import router
from app.stocks import stocks_router
from app.ingestion import ingestion_router

app = FastAPI()

app.include_router(router)
app.include_router(stocks_router)
app.include_router(ingestion_router)