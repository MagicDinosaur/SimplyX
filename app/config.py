import os

class Config:
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_DB', 'twitter_db'),
        'host': os.environ.get('MONGO_URI', 'mongodb://localhost:27017/twitter_db')
    }
