from app import app, db
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column

class Sale(db.Model):
    REGION_LEN = 40
    COUNTRY_LEN = 40
    ITEM_TYPE_LEN = 20
    SALES_CHANNEL_LEN = 7
    ORDER_PRIORITY_LEN = 1

    __tablename__ = 'Sale'
    region: Mapped[str] = mapped_column(db.String(REGION_LEN))
    country: Mapped[str] = mapped_column(db.String(COUNTRY_LEN))
    item_type: Mapped[str] = mapped_column(db.String(ITEM_TYPE_LEN))
    sales_channel: Mapped[str] = mapped_column(db.String(SALES_CHANNEL_LEN))
    order_priority: Mapped[str] = mapped_column(db.String(ORDER_PRIORITY_LEN))
    order_date: Mapped[date] = mapped_column(db.Date)
    order_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    ship_date: Mapped[date] = mapped_column(db.Date)
    units_sold: Mapped[int] = mapped_column(db.Integer)
    unit_price: Mapped[float] = mapped_column(db.Numeric(10,2))
    unit_cost: Mapped[float] = mapped_column(db.Numeric(10,2))
    total_revenue: Mapped[float] = mapped_column(db.Numeric(10,2))
    total_cost: Mapped[float] = mapped_column(db.Numeric(10,2))
    total_profit: Mapped[float] = mapped_column(db.Numeric(10,2))

with app.app_context():
    db.create_all()