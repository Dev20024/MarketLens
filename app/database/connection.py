from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://marketlens:marketlens_dev@localhost:5432/marketlens"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


