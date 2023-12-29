from mongoengine import Document, StringField, IntField, ReferenceField, ListField
from app.config import Config

# Connect to MongoDB using the configuration settings
db = Config()
db.init_app()

class Tweet(Document):
    def __init__(self, tweet_id, content, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tweet_id = tweet_id
        self.content = content
        self.user = user


    tweet_id = IntField(required=True, unique=True)
    content = StringField(required=True, max_length=280)
    user = ReferenceField('User', reverse_delete_rule=2)

    def to_dict(self):
        return {
            'tweet_id': self.tweet_id,
            'content': self.content,
            'user_id': str(self.user.id) if self.user else None
        }

class User(Document):
    user_id = IntField(required=True, unique=True)
    username = StringField(required=True, max_length=50)
    following = ListField(ReferenceField('self'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'following': [str(user.id) for user in self.following]
        }
