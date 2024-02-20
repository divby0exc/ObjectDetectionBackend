from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from user import User
from datetime import datetime
import os
from env_var_file import set_env

set_env()

username=os.getenv("atlas_user")
password=os.getenv("atlas_pwd")

uri="mongodb+srv://"+username+":"+password+"@objectdetection.mmi1vuf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
def find(user_obj):
    try:
        client.admin.command('ping')
        # Opening database users_db
        db = client["users_db"]

        # Creating a users collection
        users = db.users

        users.insert_one(user_obj.format_user())
    except Exception as e:
        print(e)

    
