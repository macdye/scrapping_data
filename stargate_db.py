import pandas.io.sql
import sqlalchemy

def drop_index(my_df):
  my_df.reset_index(drop=True, inplace=True)

sql_engine = sqlalchemy.create_engine("postgres://adytqcrkolageu:97a16fa1a6d9bf1cbe925bcfe86d53fbac12d2a8acec3dcb4f88860a9c14a3cb@ec2-52-48-65-240.eu-west-1.compute.amazonaws.com:5432/d4cd6ggafr9d27")
dbcon = sql_engine.connect()
sql_db = pandas.io.sql.SQLDatabase(sql_engine)

def insert_table(my_df,my_table):
  if not sql_db.has_table(my_table):
    args = [my_table, sql_db]
    kwargs = {
        "frame": my_df,
        "index": True,
        "index_label": "id",
        "keys": "id"
    }
    sql_table = pandas.io.sql.SQLTable(*args, **kwargs)
    sql_table.create()
  my_df.to_sql(my_table, dbcon, if_exists='append', index=False)



