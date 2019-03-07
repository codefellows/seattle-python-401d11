from flask import render_template, flash, redirect, url_for, session, abort, g
from .models import db, User
from .forms import AuthForm
from . import app
import functools


def login_required(view):
    """
    View function decorator.
    Restricts access to decorated route
    If user (g.user) not found then 404
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(404)
            # return redirect(url_for('.login'))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        if not email or not password:
            error = 'Invalid email or password'
        if User.query.filter_by(email=email).first() is not None:
            error = f'{ email } has already been registered.'

        if error is None:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()

            flash('Registration complete. Please log in.')
            return redirect(url_for('.login'))

        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        user = User.query.filter_by(email=email).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Invalid username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('.weather_detail'))

        flash(error)

    return render_template('auth/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    """
    session.clear()
    flash('Thanks for being awesome!')
    return redirect(url_for('.login'))
