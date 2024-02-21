from create_db_conn import create_connection
from execute_queries import query_to_db
from mysql.connector import Error

def fetch_user(user_to_search:str):
    user_to_search = (user_to_search,)
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username, password FROM users WHERE username= (%s)")
    cur.execute(sql, user_to_search)
    # Call upon jwt to authenticate user
    user=None
    for username, password in cur:
        user=(username,password)
    if user is None:
        return "Username or Password not found"
    else:
        return user

print(fetch_user("dkani"))