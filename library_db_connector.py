import mysql.connector as mysql

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Library_db"
    )
    return connection
