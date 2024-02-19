from mongoengine import Document, DateTimeField, StringField, UUIDField

class User(Document):
    primary_key = UUIDField()
    username = StringField(required=True, unique=True, min_length=3, max_length=20)
    password = StringField(required=True, min_length=6, max_length=20)
    created_at = DateTimeField()
    updated_at = DateTimeField()