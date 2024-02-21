from create_db_conn import create_connection

def save_table():
    conn = create_connection("localhost","root","","object_detection")
    cur=conn.cursor()
    SQL="""CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE,
        password LONGBLOB,
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