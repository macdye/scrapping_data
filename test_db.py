import pandas as pd
import sqlalchemy

sql_engine = sqlalchemy.create_engine(
    "postgres://adytqcrkolageu:97a16fa1a6d9bf1cbe925bcfe86d53fbac12d2a8acec3dcb4f88860a9c14a3cb@ec2-52-48-65-240.eu-west-1.compute.amazonaws.com:5432/d4cd6ggafr9d27")
dbcon = sql_engine.connect()

df = pd.read_sql("episodes", dbcon)
print(df)


