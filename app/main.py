from fastapi import FastAPI

# import API routers
from routes import router
from stocks import stocks_router

app = FastAPI()

app.include_router(router)
app.include_router(stocks_router)
