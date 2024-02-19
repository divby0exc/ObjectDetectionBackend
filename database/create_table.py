from mongoengine import connect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from user import User
from uuid import uuid4
from datetime import datetime
import os
from environs import Env
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

# dani = User(
#     primary_key=uuid4(),
#     username="dani",
#     password="1234567",
#     created_at=datetime.now()
# )

# dani.save()