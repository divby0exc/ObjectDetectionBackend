from execute_queries import query_to_db
from create_db_conn import create_connection

def save(user_obj):
    conn = create_connection("localhost", "root", "", "users_db")
    
    

save("aaaa")