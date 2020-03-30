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

    data = {'title': request.args['title'], 'content': request.args['content']}

    blog = Blog(data)
    user_info = google_auth.get_user_info()
    user = User.find_by_email(user_info['email'])
    blog.author_id = user.id
    blog.save()

    return Response(status=201)


@blog_api.route('/<int:blog_id>', methods=['GET'])
def blog_show(blog_id):
    blog = Blog.query.get(blog_id)
    data = blog_schema.dump(blog)
    return custom_response(data, 200)


@user_api.route('/', methods=['GET'])
def user_index():
    users = User.all()
    data = user_schema.dump(users, many=True)
    return custom_response(data, 200)


@user_api.route('/<int:user_id>', methods=['GET'])
def user_show(user_id):
    user = User.query.get(user_id)
    if not user:
        return custom_response({'error': 'user not found'}, 404)

    blogs = Blog.query.filter_by(author_id=user_id).all()
    data = blog_schema.dump(blogs, many=True)
    return custom_response(data, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
