from create_db_conn import create_connection
from mysql.connector import Error

def fetch_user(user_to_search:str, user_pwd:str=None):
    user_to_search = (user_to_search, user_pwd)
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username, password FROM users WHERE username= %s AND password= %s")
    cur.execute(sql, user_to_search)
    # Call upon jwt to authenticate user
    user=None
    for username, password in cur:
        user=(username,password)
    if user is None:
        return "Username or Password not found"
    else:
        return user

def user_exists(user_to_search:str):
    user_to_search = (user_to_search,)
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username FROM users WHERE username= %s")
    cur.execute(sql, user_to_search)
    
    user=None
    if user_to_search in cur:
        return True
    else:
        return False
