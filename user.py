from mongoengine import Document, DateTimeField, StringField, UUIDField

class User(Document):
    def __init__(self,username,password):
        primary_key = UUIDField()
        username = StringField(regex="[A-Za-z0-9]+-_\.", required=True, unique=True, min_length=3, max_length=20)
        password = StringField(regex="[A-Za-z0-9]+!@#\$%\^&\*\(\)_-\+=\[\]\{\};':\",\./<>\?\\\|", required=True, min_length=6, max_length=20)
        created_at = DateTimeField()
        updated_at = DateTimeField()