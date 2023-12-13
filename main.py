from models import Sale
from app import app

def get_rows(country: str,prio: str) -> list[Sale]:
    with app.app_context():
        rows: list[Sale] = Sale.query.filter_by(country = country, order_priority = prio).all()
        return rows

def print_results(data: list[Sale]) -> None:
    total_total_revenue = 0
    total_total_cost = 0
    total_total_profit = 0

    print('=' * 54)
    for sale in data:
        print(f'| {"Order ID".ljust(10, ".")}{str(sale.order_id).rjust(40, ".")} |')
        print(f'| {"Order Priority".ljust(15, ".")}{str(sale.order_priority).rjust(35, ".")} |')
        print(f'| {"Sales Channel".ljust(15, ".")}{str(sale.sales_channel).rjust(35, ".")} |')
        print(f'| {"Region".ljust(10, ".")}{str(sale.region).rjust(40, ".")} |')
        print(f'| {"Country".ljust(10, ".")}{str(sale.country).rjust(40, ".")} |')
        print(f'| {"Order Date".ljust(10, ".")}{str(sale.order_date).rjust(40, ".")} |')
        print(f'| {"Ship Date".ljust(10, ".")}{str(sale.ship_date).rjust(40, ".")} |')
        print(f'| {"Item Type".ljust(10, ".")}{str(sale.item_type).rjust(40, ".")} |')
        print(f'| {"Units Sold".ljust(10, ".")}{str(sale.units_sold).rjust(40, ".")} |')
        print(f'| {"Unit Price".ljust(10, ".")}{str(sale.unit_price).rjust(40, ".")} |')
        print(f'| {"Unit Cost".ljust(10, ".")}{str(sale.unit_cost).rjust(40, ".")} |')
        print(f'| {"Total Revenue".ljust(15, ".")}{str(sale.total_revenue).rjust(35, ".")} |')
        print(f'| {"Total Cost".ljust(10, ".")}{str(sale.total_cost).rjust(40, ".")} |')
        print(f'| {"Total Profit".ljust(15, ".")}{str(sale.total_profit).rjust(35, ".")} |')
        print('=' * 54)
        total_total_revenue += sale.total_revenue
        total_total_cost += sale.total_cost
        total_total_profit += sale.total_profit
    print(f'| {"Total Revenue".ljust(15, ".")}{str(total_total_revenue).rjust(35, ".")} |')
    print(f'| {"Total Cost".ljust(10, ".")}{str(total_total_cost).rjust(40, ".")} |')
    print(f'| {"Total Profit".ljust(15, ".")}{str(total_total_profit).rjust(35, ".")} |')
    print('=' * 54)

if __name__ == '__main__':
    country = input('Enter country: ')
    prio = input('Enter order priority: ')
    data = get_rows(country, prio)
    if data:
        print_results(data)
    else:
        print('No orders found.')