from app import app, db
from models import Sale
from datetime import date, datetime
import csv

def convert_american_to_date(american_date: str) -> date:
    month = american_date.split('/')[0]
    day = american_date.split('/')[1]
    year = american_date.split('/')[2]
    
    iso_date = year
    if len(month) < 2:
        month = '0' + month
    iso_date += month
    if len(day) < 2:
        day ='0' + day
    iso_date += day
    
    converted_date  = date.fromisoformat(iso_date)
    return converted_date

def import_from_csv(file) -> None:
    with open(file, 'r') as file:
        csvreader = csv.DictReader(file, delimiter=',')
        with app.app_context():
            for row in csvreader:
                if row['Region'] != 'Region':
                    sale = Sale()
                    sale.region = row['Region']
                    sale.country = row['Country']
                    sale.item_type = row['Item Type']
                    sale.sales_channel = row['Sales Channel']
                    sale.order_priority = row['Order Priority']
                    sale.order_date = convert_american_to_date(row['Order Date'])
                    sale.order_id = int(row['Order ID'])
                    sale.ship_date = convert_american_to_date(row['Ship Date'])
                    sale.units_sold = int(row['Units Sold'])
                    sale.unit_price = float(row['Unit Price'])
                    sale.unit_cost = float(row['Unit Cost'])
                    sale.total_revenue = float(row['Total Revenue'])
                    sale.total_cost = float(row['Total Cost'])
                    sale.total_profit = float(row['Total Profit'])
                    db.session.add(sale)
            db.session.commit()

if __name__ == '__main__':
    opt = input('Import 100 or 5m? ')
    start = datetime.now()
    if opt == '5m':
        import_from_csv('5mSalesRecords.csv')
    elif opt == '100':
        import_from_csv('100SalesRecords.csv')
    else:
        print('Unrecognised option. No import.')
        quit()
    end = datetime.now()
    print(f'Import completed. Took {(end - start).total_seconds()} seconds.')