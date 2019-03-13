from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(256), index=True)
    zipcode = db.Column(db.String(256), index=True, unique=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<City {}-{}>'.format(self.name, self.zipcode)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(256), index=True)

    cities = db.relationship('City', backref='category', lazy=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Category {}>'.format(self.name)


class User(db.Model):
    """
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), index=True, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    categories = db.relationship('Category', backref='user', lazy=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def __init__(self, email, password):
        self.email = email
        self.password = sha256_crypt.hash(password)

    @classmethod
    def check_password_hash(cls, user, password):
        """
        """
        if user is not None:
            if sha256_crypt.verify(password, user.password):
                return True

        return False