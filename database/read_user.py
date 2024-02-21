from create_db_conn import create_connection
from execute_queries import query_to_db
from mysql.connector import Error

def fetch_user(user_to_search:str):
    conn = create_connection("localhost", "root", "", "object_detection")
    sql="SELECT username, password FROM users WHERE username="+user_to_search
    try:
        fetched_user=query_to_db(conn, sql)
        # Call upon jwt to authenticate user
        print(fetched_user)
    except Error as e:
        print(f"Error {e} occured")

# fetch_user()