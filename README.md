# Daily Reports

This project is designed to help you manage daily reports. It involves creating and maintaining a database to store your daily report data from receipts.

## Getting Started

To set up the database, follow these steps:

1. Open `CRUD.py`.
2. Comment out the line `database="reportsdb"` within the `mysql.connector.connect` block:
   
   ```python
   mydb = mysql.connector.connect(
       host=host,
       user=user,
       password=password,
       # database="reportsdb"
   )
   ```
Run the push_data.py program. Choose the option to create the database.

Exit the program and uncomment the line database="reportsdb" within the mysql.connector.connect block in CRUD.py:

   
   ```python
   mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database="reportsdb"
   )
```

Run push_data.py again. This time, you can create tables and import data from files.

Finally, you can generate the final report.

## Note<br>
Make sure to replace host, user, password, and any other relevant parameters with your actual database connection details.
The best way to add them is to store in .env file.

Feel free to reach out if you encounter any issues or need further assistance.