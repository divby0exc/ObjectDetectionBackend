from mongoengine import Document, DateTimeField, StringField, UUIDField
import base64

class User(Document):
    username = StringField(required=True, unique=True, min_length=3, max_length=20)
    password = StringField(required=True, min_length=6, max_length=20)
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def format_user(self):
        self.password=base64.b64encode(bytes(self.password))
        return self.to_mongo()