import mysql.connector
from mysql.connector import Error

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Library_db"
    )
    return connection


def connect_db():
    db_name = 'library_db'   
    user = 'root'
    password = '12@Wsxdr56'
    host = '127.0.0.1'
    Port = '3306'
    SSL = 'enabled with TLS_AES_128_GCM_SHA256'  
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )

    
    try: 
        conn= mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
            )

        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    
    except Error as e:
        print(f"Error{e}")
        return None
    


    