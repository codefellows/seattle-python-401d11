from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .models import Category


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
        self.categories.choices = [(str(c.id), c.name) for c in Category.query.all()]


class CategoryCreateForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])
