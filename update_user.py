from create_db_conn import create_connection
from datetime import datetime

def update_user(new_pwd:str, username:str):
    conn=create_connection("localhost","root","","object_detection")
    cur=conn.cursor()
    sql=("UPDATE users SET updated_at=%s, hashed_pwd=%s "
        "WHERE username=%s")
    vals=(datetime.now(), new_pwd, username)
    cur.execute(sql,vals)
    conn.commit()
