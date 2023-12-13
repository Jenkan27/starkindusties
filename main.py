from models import Sale
from app import app, db 







def get_rows(country: str,prio: str) -> list[Sale]:
    with app.app_context():
        rows: list[Sale] = Sale.query.filter_by(country = country, order_priority = prio).all()
        return rows
    
for sale in get_rows('Bulgaria', 'M'):
    print(sale)