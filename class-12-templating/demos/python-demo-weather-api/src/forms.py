from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CityForm(FlaskForm):
    """
    """
    zipcode = StringField('zipcode', validators=[DataRequired()])


class CityAddForm(FlaskForm):
    """
    """
    zipcode = StringField('zipcode', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
