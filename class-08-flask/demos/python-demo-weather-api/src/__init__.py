from flask import Flask
import os


basedir = os.path.abspath(os.path.dirname(__file__))


# `flask run` - runs application on local server
app = Flask(__name__, static_url_path='', static_folder='static', instance_relative_config=True)

app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


from . import routes, models, exceptions
