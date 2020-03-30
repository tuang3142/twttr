import os
import json
import google_auth
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", default=False)
    app.register_blueprint(google_auth.app)
    db.init_app(app)

    @app.route('/')
    def index():
        if google_auth.is_logged_in():
            user_info = google_auth.get_user_info()
            return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

        return 'You are not currently logged in.'
    return app
