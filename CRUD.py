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


def create_database():
    mycursor.execute("CREATE DATABASE reportsdb")


def create_table():
    mycursor.execute(
        "CREATE TABLE Reports (id int PRIMARY KEY AUTO_INCREMENT, storeid int, quantity int, total_paid_amount float)")


def insert_into(store_id, quantity, total_paid_amount):
    """
    Inserting data to mysql database by CRUD
    """
    for i in range(len(store_id)):
        sql = """INSERT INTO reportsdb.reports (storeid, quantity, total_paid_amount) VALUES (%s, %s, %s)"""
        values = (store_id[i], quantity[i], total_paid_amount[i])
        mycursor.execute(sql, values)
        mydb.commit()


def get_data_from_db():
    """
    Getting data from mysql database from reports table
    :return: adding that data to pandas dataframe
    """
    query = "SELECT storeid,quantity,total_paid_amount  FROM reportsdb.reports"
    df = pd.read_sql(query, mydb, columns=['storeid', 'quantity', 'total_paid_amount'])
    return df
