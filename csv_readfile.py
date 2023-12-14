import csv
from app import app, db
from datetime import date, datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Sale


class DataBaseLoader:
    def __init__(self, app: Flask, db: SQLAlchemy) -> None:
        self._app = app
        self._db = db

    def csv_to_database(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            print(f'CSV file "{csv_file}" loaded.')
            row_count = 0
            for row in csv_reader:
                row_count += 1
            print(f'Detecting {row_count} entries.')
            file.seek(0)
            if row_count <= 10000:
                count = 0
                for row in csv_reader:
                    if row['Region'] == 'Region':
                        continue
                    self._create_sale(row)
                    count += 1
                    if count % 100 == 0:
                        timestamp = datetime.now()
                        print(f'[{timestamp}]: {count} rows processed...')
            else:
                print('File too big.')
    
    def _create_sale(self, data: dict[str, str]) -> None:
        with self._app.app_context():
            sale = Sale()
            sale.region = data['Region']
            sale.country = data['Country']
            sale.item_type = data['Item Type']
            sale.sales_channel = data['Sales Channel']
            sale.order_priority = data['Order Priority']
            sale.order_date = self._convert_american_to_date(data['Order Date'])
            sale.order_id = int(data['Order ID'])
            sale.ship_date = self._convert_american_to_date(data['Ship Date'])
            sale.units_sold = int(data['Units Sold'])
            sale.unit_price = float(data['Unit Price'])
            sale.unit_cost = float(data['Unit Cost'])
            sale.total_revenue = float(data['Total Revenue'])
            sale.total_cost = float(data['Total Cost'])
            sale.total_profit = float(data['Total Profit'])
            db.session.add(sale)
            db.session.commit()

    def _convert_american_to_date(self, american_date: str) -> date:
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
                        

if __name__ == '__main__':
    db_loader = DataBaseLoader(app, db)
    opt = input('Import 100 or 5m? ')
    start = datetime.now()
    if opt == '5m':
        db_loader.csv_to_database('5mSalesRecords.csv')
    elif opt == '100':
        db_loader.csv_to_database('100SalesRecords.csv')
    else:
        print('Unrecognised option. No import.')
        quit()
    end = datetime.now()
    print(f'Import completed. Took {(end - start).total_seconds()} seconds.')