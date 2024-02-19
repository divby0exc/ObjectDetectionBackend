from mongoengine import connect
from user import User
from uuid import uuid4
from datetime import datetime

connect(host="mongodb://127.0.0.1:27017/users")

dani = User(
    primary_key=uuid4(),
    username="dani",
    password="1234567",
    created_at=datetime.now()
)

dani.save()