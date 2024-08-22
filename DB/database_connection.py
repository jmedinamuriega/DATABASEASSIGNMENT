import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name="gym_db"
    user="root"
    password = "Gringochone0"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
            )
        if conn.is_connected():
            print("Connected to MySQL database successfully")
            return conn
       
    except Error as e:
        print(f"error:{e}")
        return None

connect_database()