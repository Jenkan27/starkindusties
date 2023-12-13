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
    list_from_file = []

    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        
        first_row = True
        for row in csvreader:
            if first_row:
                row_title = []
                for element in row:
                    row_title.append(element)
                first_row = False
                continue
            row_dict = {}
            index = 0
            
            while index < len(row):
                for element in row:
                    row_dict[row_title[index]] = element
                    index += 1
            list_from_file.append(row_dict)

    with app.app_context():
        for line in list_from_file:
            sale = Sale()
            sale.region = line['Region']
            sale.country = line['Country']
            sale.item_type = line['Item Type']
            sale.sales_channel = line['Sales Channel']
            sale.order_priority = line['Order Priority']
            sale.order_date = convert_american_to_date(line['Order Date'])
            sale.order_id = int(line['Order ID'])
            sale.ship_date = convert_american_to_date(line['Ship Date'])
            sale.units_sold = int(line['Units Sold'])
            sale.unit_price = float(line['Unit Price'])
            sale.unit_cost = float(line['Unit Cost'])
            sale.total_revenue = float(line['Total Revenue'])
            sale.total_cost = float(line['Total Cost'])
            sale.total_profit = float(line['Total Profit'])
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