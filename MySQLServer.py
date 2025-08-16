import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="King99",
    )

    my_cursor = mydb.cursor()
    try:
        # Create the database
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

    my_cursor.close()
    mydb.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password is incorrect.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
else:
    mydb.close()