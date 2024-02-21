from create_db_conn import create_connection
from user import User
from read_user import user_exists
from datetime import datetime

def save(user_obj: User):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("INSERT INTO users "
        "(username, password, updated_at) "
        "VALUES (%s, %s, %s)")
    vals=(user_obj.get_username(),user_obj.get_pwd(),datetime.now())
    if user_exists(user_obj.username):
        cur.execute(sql, vals)
    else:
        sql=sql.replace("updated_at", "created_at")
        cur.execute(sql,vals)
    
    conn.commit()
    

dani = User("brobro", "123457")
save(dani)