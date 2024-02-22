from create_db_conn import create_connection

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

delete_user("brobroo")