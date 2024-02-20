import psycopg2
from psycopg2 import OperationalError
from create_db_conn import create_connection
from create_database import create_DB


connection = create_connection(
    "postgres", "postgres", "abc123", "127.0.0.1", "5432"
)

create_DB_query="CREATE DATABASE users_db"
create_DB(conn=connection, query=create_DB_query)

# try:
#     connection = create_connection(
#     "users_db", "postgres", "abc123", "127.0.0.1", "5432"
#     )
#     print(f"Connection info {connection.info}")
# except OperationalError as e:
#     print(f"Error: {e}")
    
