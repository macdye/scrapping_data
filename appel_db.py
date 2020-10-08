#heroku pg:psql -a scrapping-stargate
import pandas as pd
import sqlalchemy
from main import df_series

sql_engine = sqlalchemy.create_engine(
    "postgres://adytqcrkolageu:97a16fa1a6d9bf1cbe925bcfe86d53fbac12d2a8acec3dcb4f88860a9c14a3cb@ec2-52-48-65-240.eu-west-1.compute.amazonaws.com:5432/d4cd6ggafr9d27")
dbcon = sql_engine.connect()

df_series = pd.read_sql_table("series", dbcon)
#print(df_series)
df_diffusions_date = pd.read_sql_table("diffusion_dates", dbcon)
#print(df_diffusions_date)
