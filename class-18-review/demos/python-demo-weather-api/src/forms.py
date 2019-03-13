from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .models import Category
from flask import g


class CityForm(FlaskForm):
    """
    """
    zipcode = StringField('zipcode', validators=[DataRequired()])


class CityAddForm(FlaskForm):
    """
    """
    zipcode = StringField('zipcode', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    categories = SelectField('categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories.choices = [(str(c.id), c.name) for c in Category.query.filter_by(user_id=g.user.id).all()]


class CategoryCreateForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])


class AuthForm(FlaskForm):
    """
    """
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
