from execute_queries import query_to_db
from create_db_conn import create_connection
import mysql.connector
from user import User

def save(user_obj: User):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = query_to_db.connection.cursor()
    cur.execute
    sql=f"INSERT INTO users (username, password) \
        VALUES (%s, %s)"
    # "INSERT INTO employees (first_name) VALUES (%s), (%s)"
    query_to_db(conn, sql)
    conn.commit()
    

dani = User("dani", "123456")
save(dani)