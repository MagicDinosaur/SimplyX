from flask import Flask
from flask_restful import Api
from controllers import TweetController

app = Flask(__name__)
api = Api(app)

api.add_resource(TweetController, '/tweet/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)