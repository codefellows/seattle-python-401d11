from flask import render_template, redirect, url_for, flash, session
from sqlalchemy.exc import DBAPIError, IntegrityError
from .forms import CityForm, CityAddForm
from .models import db, City
from . import app
import requests
import json
import os


@app.route('/')
def home():
    """
    """

    # foods = {
    #     "candy" : 'snickers (frozen)',
    #     "snack" : 'chips',
    #     "late_night" : 'salsa'
    # }

    foods = (
        'snickers',
        'lasagna',
        'juice'
    )

    return render_template('home.html', foods=foods)


def get_fave_snack():
    return 'canoli'

@app.route('/search', methods=['GET', 'POST'])
def company_search():
    """
    """
    form = CityForm()

    if form.validate_on_submit():
        zipcode = form.data['zipcode']

        url = '{}/weather?zip={}&APPID={}'.format(
            os.environ.get('API_URL'),
            zipcode,
            os.environ.get('API_KEY'),
        )

        res = requests.get(url)
        data = json.loads(res.text)
        session['context'] = data
        session['zipcode'] = zipcode

        return redirect(url_for('.preview_weather'))

    return render_template('weather/search.html', form=form)


@app.route('/preview', methods=['GET', 'POST'])
def preview_weather():
    """
    """
    form_context = {
        'name': session['context']['name'],
        'zipcode': session['zipcode'],
    }
    form = CityAddForm(**form_context)

    if form.validate_on_submit():
        try:
            city = City(name=form.data['name'], zipcode=form.data['zipcode'])
            db.session.add(city)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. Something went wrong with your search.')
            return render_template('weather/search.html', form=form)

        return redirect(url_for('.weather_detail'))

    return render_template(
        'weather/preview.html',
        form=form,
        zipcode=form_context['zipcode'],
        weather_data=session['context'],
    )


@app.route('/weather')
def weather_detail():
    """
    """
    cities = City.query.all()
    return render_template('weather/weather.html', cities=cities)
