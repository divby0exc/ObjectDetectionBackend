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

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Opening database users_db
db = client["users_db"]

dani = User(username="Dani", password="1234567", created_at=datetime.now())

# Creating a users collection
users = db.users

user_id = users.insert_one(dani.format_user()).inserted_id

print("UserID:",user_id)

print(db.list_collection_names())