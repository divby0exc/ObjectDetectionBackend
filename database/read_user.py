from create_db_conn import create_connection
from execute_queries import query_to_db
from mysql.connector import Error

def fetch_user(user_to_search:str):
    user_obj = tuple(user_to_search)
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username, password FROM users WHERE username=%s")
    try:
        cur.execute(sql, user_obj)
        # Call upon jwt to authenticate user
        user=None
        for username, password in cur:
            user=(username,password)
        print(user)
        print(type(user))
        print(user is None)
    except Error as e:
        print(f"Error {e} occured")

fetch_user("dani")