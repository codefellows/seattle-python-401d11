from flask import render_template, redirect, url_for, flash, session, g
from .forms import CityForm, CityAddForm, CategoryCreateForm
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, City, Category
from .auth import login_required
from . import app
import requests
import json
import os


@app.add_template_global
def get_categories():
    """
    """
    return Category.query.filter_by(user_id=g.user.id).all()


@app.route('/')
def home():
    """
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
@login_required
def city_search():
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
@login_required
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
            city = City(
                name=form.data['name'],
                zipcode=form.data['zipcode'],
                category_id=form.data['categories'],
            )
            db.session.add(city)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. Something went wrong with your search.')
            db.session.rollback()
            return render_template('weather/search.html', form=form)

        return redirect(url_for('.weather_detail'))

    return render_template(
        'weather/preview.html',
        form=form,
        zipcode=form_context['zipcode'],
        weather_data=session['context'],
    )


@app.route('/weather', methods=['GET', 'POST'])
@login_required
def weather_detail():
    """
    """
    form = CategoryCreateForm()

    if form.validate_on_submit():
        try:
            category = Category(name=form.data['name'], user_id=g.user.id)
            db.session.add(category)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. Something went wrong with your Category Form.')
            return render_template('weather/weather.html', form=form)

        return redirect(url_for('.city_search'))

    user_categories = Category.query.filter(Category.user_id == g.user.id).all()
    cat_ids = [c.id for c in user_categories]

    cities = City.query.filter(City.category_id.in_(cat_ids)).all()
    return render_template('weather/weather.html', cities=cities, form=form)
