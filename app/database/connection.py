import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#"postgresql+psycopg://marketlens:marketlens_dev@localhost:5432/marketlens"
DATABASE_URL = os.environ("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


