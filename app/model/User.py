from mongoengine import Document, StringField, ReferenceField, ListField

class User(Document):
    user_id = StringField(required=True, unique=True)
    username = StringField(required=True, max_length=50)
    followers = ListField(ReferenceField('self'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'followers': [follower.user_id for follower in self.followers]
        }
