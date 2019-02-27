# Flask application boilerplate for Weather App

1. Clone repo
1. Ensure that `.env` file contains the below configs
    1. Add any additional details for values, such as username and password for `DATABASE_URL`
1. Create Virtualenv & Activate
    1. Ensure that you have a tool for loading env vars (dotenv, pipenv, etc)
1. Create a Database in PostgreSQL called `weather`
1. 'Upgrade' migrations to DB
    1. `flask db upgrade`
    1. If `migrations/` directory is not present first run:
        1. `flask db init`
        1. `flask db migrate -m 'initial migration'`
        1. THEN...
        1. `flask db upgrade`
1. Start the server: `flask run`


### ENV Vars
```dotenv
FLASK_APP=src/wsgi.py
FLASK_ENV=development
DATABASE_URL=postgres://localhost:5432/weather
SECRET_KEY=5a9143ae-c439-4ea1-8228-5d67da63d1e4  # Generate a UUID with `python3 -c "import UUID; print(UUID.UUIDv4())"` 
API_URL=http://api.openweathermap.org/data/2.5  
API_KEY=75a7450d79ddcdbf8ceef630bf21766b  # Get your API KEY from OpenWeatherMap.org - It's free
```
