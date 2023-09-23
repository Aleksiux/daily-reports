import mysql.connector
from dotenv import dotenv_values

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

    sql = """INSERT INTO Reports (storeid, quantity, unit_cost_price) VALUES (%s, %s, %s)"""
    value = (store_id, quantity, unit_cost_price)
    mycursor.execute(sql, value)
    mydb.commit()


mycursor.execute("SELECT * FROM reportsdb.reports")

# for x in mycursor:
#     print(x)
