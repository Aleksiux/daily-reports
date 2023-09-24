from CRUD import get_data_from_db


df = get_data_from_db()
agg_df = df.groupby('storeid').agg({'quantity': 'sum', 'total_paid_amount': 'sum'}).reset_index()
agg_df.columns = ['StoreID', 'TotalItems', 'TotalAmount']
print(agg_df)