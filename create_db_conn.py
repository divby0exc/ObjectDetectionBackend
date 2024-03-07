import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_pwd, db=None):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_pwd,
            database=db
        )
        print("Connection to DB successful")
    except Error as e:
        print(f"Error: {e} occured")
    
    return conn

# query_to_db(create_connection("localhost","root",""))
