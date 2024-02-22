from create_db_conn import create_connection
from user import User
from read_user import user_exists
from datetime import datetime
from update_user import update_user

def save(user_obj: User):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("INSERT INTO users "
        "(username, hashed_pwd, created_at) "
        "VALUES (%s, %s, %s)")
    vals=(user_obj.get_username(),user_obj.get_pwd(),datetime.now())
    if user_exists(user_obj.username):
        update_user(user_obj.password, user_obj.username)
    else:
        cur.execute(sql,vals)
        conn.commit()
    

dani = User("brobroo", "123457")
save(dani)