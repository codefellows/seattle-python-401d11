from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    zipcode = db.Column(db.String(256), index=True, unique=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<City {}-{}>'.format(self.name, self.zipcode)
