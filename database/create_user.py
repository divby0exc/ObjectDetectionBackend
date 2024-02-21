from execute_queries import query_to_db
from create_db_conn import create_connection
import mysql.connector
from user import User

def save(user_obj: User):
    conn = create_connection("localhost", "root", "", "object_detection")
    cur = conn.cursor()
    sql=("INSERT INTO users "
         "(username, password) "
         "VALUES (%username(s), %(password)s)")
    vals=(user_obj,user_obj.password)
    # "INSERT INTO employees (first_name) VALUES (%s), (%s)"
    # query_to_db(conn, sql)
    cur.execute(sql,vals)
    conn.commit()
    

dani = User("dani", "123456")
save(dani.__getattribute__)