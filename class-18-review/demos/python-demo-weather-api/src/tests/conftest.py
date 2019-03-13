from src.models import City, Category, User
from src.models import db as _db
from src import app as _app
import pytest
import os


@pytest.fixture()
def app(request):
    """Session-wide Testable Flask Application
    """
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False,
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture()
def db(app, request):
    """Session-wide Test Database
    """
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture()
def session(db, request):
    """Creates a new database session for testing
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def client(app, db, session):
    """
    """
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture()
def user(session):
    """
    """
    user = User(email='default@example.com', password='secret')

    session.add(user)
    session.commit()
    return user


@pytest.fixture()
def authenticated_client(client, user):
    """
    """
    client.post(
        '/login',
        data={'email': user.email, 'password': 'secret'},
        follow_redirects=True,
    )
    return client


@pytest.fixture()
def category(session, user):
    """
    """
    category = Category(name='Default', user_id=user.id)

    session.add(category)
    session.commit()
    return category


@pytest.fixture()
def city(session, category):
    """
    """
    city = City(name='Bellevue', zipcode='98038', category_id=category.id)

    session.add(city)
    session.commit()
    return city
