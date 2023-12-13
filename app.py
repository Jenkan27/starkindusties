from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

USER = 'root'
PASS = 'password'
DB_NAME = 'inl2'

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASS}@localhost/{DB_NAME}'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()