from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv('./assets/winemag-data-130k-v2.csv')
df = pd.DataFrame(csv_data)

# Adjust NaN values in each column, and generally clean data set
df['id'] = df['Unnamed: 0'] + 1
del df['Unnamed: 0']

df['price'] = df['price'].fillna(0.0)
df['designation'] = df['designation'].fillna('unknown')
df['region_1'] = df['region_1'].fillna('unknown')
df['region_2'] = df['region_2'].fillna('unknown')
df['taster_twitter_handle'] = df['taster_twitter_handle'].fillna('unknown')
df['taster_name'] = df['taster_name'].fillna('unknown')
df['country'] = df['country'].fillna('unknown')
df['province'] = df['province'].fillna('unknown')
df['variety'] = df['variety'].fillna('unknown')

db_protocol = 'postgresql'
db_host = os.environ.get('DB_HOST', '')
db_user = os.environ.get('DB_USER', '')
db_password = os.environ.get('DB_PASSWORD', '')
db_name = os.environ.get('DB_NAME', '')


engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))

df.to_sql("reviews_app_review", engine, if_exists='append', index=False)
