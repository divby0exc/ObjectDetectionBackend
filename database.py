import mysql.connector
from mysql.connector import Error
from user import User
from datetime import datetime
from authenticate import dec_pwd, crypt_pwd
import json

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

# first connection when there is no table
# query_to_db(create_connection("localhost","root",""))

def save_table():
    conn = create_connection("localhost","root","","object_detection")
    cur=conn.cursor()
    SQL="""CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        hashed_pwd LONGBLOB NOT NULL,
        created_at DATETIME,
        updated_at DATETIME
    )"""
    cur.execute(SQL)
    conn.commit()

# conn = create_connection("localhost","root","")
# cur=conn.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS object_detection")
# conn.commit()
# save_table()

def save(user_obj: User):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("INSERT INTO users "
        "(username, hashed_pwd, created_at) "
        "VALUES (%s, %s, %s)")
    vals=(user_obj.get_username(),crypt_pwd(user_obj.get_pwd()),datetime.now())
    if user_exists(user_obj.username):
        update_user(user_obj.password, user_obj.username)
    else:
        cur.execute(sql,vals)
        conn.commit()
    

# dani = User("brobroo", "123457")
# save(dani)

def fetch_user(user_to_search:str):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("SELECT username, hashed_pwd FROM users WHERE username= %s")
    cur.execute(sql, (user_to_search,))
    # Call upon jwt to authenticate user
    user= cur.fetchone()
    if user is None:
        return None
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

def update_user(new_pwd:str, username:str):
    conn=create_connection("localhost","root","","object_detection")
    cur=conn.cursor()
    sql=("UPDATE users SET updated_at=%s, hashed_pwd=%s "
        "WHERE username=%s")
    vals=(datetime.now(), crypt_pwd(new_pwd), username)
    cur.execute(sql,vals)
    conn.commit()

def delete_user(username:str):
    conn = create_connection("localhost","root", "", "object_detection")
    cur=conn.cursor()
    sql="DELETE FROM users WHERE username=%s"
    val=(username,)
    confirmation=input("Enter username: "+username+"\n")
    if confirmation == username:
        cur.execute(sql,val)
        conn.commit()
        print("User",username, "deleted")
    else:
        print("Wrong username")

# delete_user("brobroo")