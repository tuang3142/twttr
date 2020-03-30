from .schemas import BlogSchema, UserSchema
from .models import Blog, User
from flask import request, json, Response, Blueprint
from . import google_auth

blog_api = Blueprint('blogs', __name__)
blog_schema = BlogSchema()

user_api = Blueprint('users', __name__)
user_schema = UserSchema()


@blog_api.route('/', methods=['GET'])
def blog_index():
    blogs = Blog.all()
    data = blog_schema.dump(blogs, many=True)
    return custom_response(data, 200)


@blog_api.route('/', methods=['POST'])
def blog_create():
    if not google_auth.is_logged_in():
        return custom_response("you need to login", 403)

    req = request.get_json()
    data, error = blog_schema.load(req, partial=True)

    if error:
        return custom_response(error, 400)

    blog = Blog(data)
    user_info = google_auth.get_user_info()
    user = User.find_by_email(user_info['email'])
    blog.author_id = user.id
    blog.save()

    return Response(status=200)


@user_api.route('/', methods=['GET'])
def user_index():
    users = User.all()
    data = user_schema.dump(users, many=True)
    return custom_response(data, 200)


@user_api.route('/me', methods=['GET'])
def user_show():
    if not google_auth.is_logged_in():
        return custom_response("you need to login", 403)
    user_info = google_auth.get_user_info()
    return custom_response(user_info, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
