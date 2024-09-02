
import mysql.connector
from mysql.connector import Error

database_name = 'Library_db'  
import mysql.connector

database_name = 'Library_db'  
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12wsxdr56",
    database=database_name 
)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12wsxdr56", 
        database="Library_db"
    )

    if conn.is_connected():
        print("Connected to MySQL database!")
    else:
        print("Failed to connect to MySQL database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
