# Testing a Flask Application

1. Scaffold `test/` with necessary files
1. `TESTING=True pytest -v`


Example `.env` 
```dotenv
FLASK_APP=src/wsgi.py
FLASK_ENV=development
DATABASE_URL=postgres://localhost:5432/weather
TEST_DATABASE_URL=postgres://localhost:5432/weather_test
SECRET_KEY=5a9143ae-c439-4ea1-8228-5d67da63d1e4
API_URL=http://api.openweathermap.org/data/2.5
API_KEY=75a7450d79ddcdbf8ceef630bf21766b
```
