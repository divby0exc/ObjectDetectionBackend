import psycopg2
from psycopg2 import OperationalError

def create_DB(conn, query):
    conn.autocommit=True
    cur=conn.cursor()
    try:
        cur.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error {e} occured")