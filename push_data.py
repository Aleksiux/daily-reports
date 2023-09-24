from CRUD import get_data_from_db
from get_data import GetReceiptData
import os
import datetime

receipt_data = GetReceiptData()


def create_final_csv_report():
    """
    Getting data from database to pandas dataframe and that dataframe aggregating to final fields
    """
    df = get_data_from_db()
    agg_df = df.groupby('storeid').agg({'quantity': 'sum', 'total_paid_amount': 'sum'}).reset_index()
    agg_df.insert(0, 'Date', datetime.date.today())
    agg_df.columns = ['Date', 'StoreID', 'TotalItems', 'TotalAmount']
    return agg_df.to_csv(f'{datetime.date.today()}_receipt.csv', index=False)


while True:
    user_input = input(
        "What you wanna do?\n1.GET data\n2.Create final CSV report\n3.Create database\n4.Create database table\n0.Exit "
        "program\n")
    if user_input == '1':
        receipt_data.get_data_and_insert()
    elif user_input == '2':
        print(f"Final report was created at: {os.getcwd()}")
        create_final_csv_report()
    elif user_input == '0':
        print("You have exited the program")
        break
    else:
        print('You can only choose from 1, 2 or 0')
