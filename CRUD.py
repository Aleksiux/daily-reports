import mysql.connector
from dotenv import dotenv_values
import pandas as pd

config = dotenv_values(".env")
host = config['host']
user = config['user']
password = config['password']

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database="reportsdb"
)

mycursor = mydb.cursor()


# mycursor.execute("CREATE DATABASE reportsdb")
# mycursor.execute(
#     "CREATE TABLE Reports (id int PRIMARY KEY AUTO_INCREMENT, storeid int, quantity int, unit_cost_price float)")
def insert_into(store_id, quantity, unit_cost_price):
    for i in range(len(store_id)):
        sql = """INSERT INTO reportsdb.reports (storeid, quantity, unit_cost_price) VALUES (%s, %s, %s)"""
        values = (store_id[i], quantity[i], unit_cost_price[i])
        mycursor.execute(sql, values)
        mydb.commit()


def get_data_from_db():
    query = "SELECT storeid,quantity,unit_cost_price  FROM reportsdb.reports"
    df = pd.read_sql(query, mydb, columns=['storeid', 'quantity', 'unit_cost_price'])
    return df
