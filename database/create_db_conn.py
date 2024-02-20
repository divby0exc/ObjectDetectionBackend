import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_pwd, db_host, db_port):
    conn = None
    try:
        conn = psycopg2.connect(
            database=db_name,
            host=db_host,
            user=db_user,
            password=db_pwd,
            port=db_port)
        
        print("Connection to PosgreSQL success")
        return conn
    except OperationalError as e:
        print(f"The error {e} occured")