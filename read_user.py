from create_db_conn import create_connection
from mysql.connector import Error
from authenticate import dec_pwd, crypt_pwd
import json

def fetch_user(user_to_search:str):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username, hashed_pwd FROM users WHERE username= %s")
    cur.execute(sql, (user_to_search,))
    # Call upon jwt to authenticate user
    user= cur.fetchone()
    if user is None:
        return "Username or Password not found"
    else:
        dec={"username":user[0],"password":user[1]}
        return dec
    

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
