import os
import json
from flask import Flask
from . import google_auth
from .models.user import User
from .models.blog import Blog
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.register_blueprint(google_auth.app)
    Migrate(app, db)
    db.init_app(app)

    @app.route('/')
    def index():
        if google_auth.is_logged_in():
            user_info = google_auth.get_user_info()
            return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

        return 'You are not currently logged in.'
    return app
