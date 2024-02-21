import mysql.connector
from mysql.connector import Error

def query_to_db(connection, query, vals=None):
    cur = connection.cursor()
    try:
        # if query is None:
        #     cur.execute("CREATE DATABASE IF NOT EXISTS object_detection")
        # else:
        cur.execute(query)
        connection.commit()
        print("Query successfully executed")
    except Error as e:
        print(f"Error: {e} occured")