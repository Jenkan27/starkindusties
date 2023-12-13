from app import app, db
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column

class Sale(db.Model):
    STRING_LEN = 2000

    __tablename__ = 'Sale'
    region: Mapped[str] = mapped_column(db.String(STRING_LEN))
    country: Mapped[str] = mapped_column(db.String(STRING_LEN))
    item_type: Mapped[str] = mapped_column(db.String(STRING_LEN))
    sales_channel: Mapped[str] = mapped_column(db.String(STRING_LEN))
    order_priority: Mapped[str] = mapped_column(db.String(STRING_LEN))
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