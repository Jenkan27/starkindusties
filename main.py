from models import Sale
from app import app, db 







def get_rows(country: str,prio: str) -> list[Sale]:
    with app.app_context():
        rows: list[Sale] = Sale.query.filter_by(country = country, order_priority = prio).all()
        return rows
    
for sale in get_rows('Bulgaria', 'M'):
    print(f'{sale.region} {sale.country} {sale.item_type} {sale.sales_channel} {sale.order_priority} {sale.order_date} {sale.order_id} {sale.ship_date} {sale.units_sold} {sale.unit_price} {sale.unit_cost} {sale.total_revenue} {sale.total_cost} {sale.total_profit}')