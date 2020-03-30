import os
import json

from flask import Flask, Response
from flask_migrate import Migrate
from . import google_auth, views, models


def create_app():
    app = Flask(__name__)

    app.url_map.strict_slashes = False

    app.secret_key = os.environ.get('SECRET_KEY')

    db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # breakpoint()
    app.register_blueprint(google_auth.google_api, url_prefix='/api/v1/google')
    app.register_blueprint(views.blog_api, url_prefix='/api/v1/blogs')
    app.register_blueprint(views.user_api, url_prefix='/api/v1/users')

    Migrate(app, models.db)

    models.db.init_app(app)

    @app.route('/')
    def index():
        if not google_auth.is_logged_in():
            return custom_response("you need to login", 403)

        return views.blog_index()

    return app


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
