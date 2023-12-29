from flask import Flask
from app.controllers import TwitterController
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.add_url_rule('/tweet/<int:user_id>', view_func=TwitterController.as_view('tweet'))

if __name__ == '__main__':
    app.run(debug=True)
