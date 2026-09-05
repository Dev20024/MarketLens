from sqlalchemy import create_engine

engine = create_engine("postgresql://bob@localhost:5432/MarketLensDatabase")