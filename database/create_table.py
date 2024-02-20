from create_db_conn import create_connection
from execute_queries import query_to_db

def save_table():
    conn = create_connection("localhost","root","","object_detection")
    SQL="""CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password LONGBLOB,
        created_at DATETIME,
        updated_at DATETIME
    )"""
    query_to_db(conn, SQL)

# save_table()