from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from datetime import date
from sqlalchemy import Date

from sqlalchemy import UniqueConstraint

from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Stock(Base):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(unique=True)
    company_name: Mapped[str]
    exchange: Mapped[str]
    sector: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    daily_prices: Mapped[list["DailyPrice"]] = relationship(back_populates="stock")

class DailyPrice(Base):
    __tablename__ = "daily_prices"
    __table_args__ = (
        UniqueConstraint("stock_id", "date", name="uq_daily_price_stock_date"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    stock_id: Mapped[int] = mapped_column(ForeignKey("stocks.id"))
    date: Mapped[date] = mapped_column(Date)
    open: Mapped[float]
    high: Mapped[float]
    low: Mapped[float]
    close: Mapped[float]
    volume: Mapped[int]

    stock: Mapped["Stock"] = relationship(back_populates="daily_prices")

