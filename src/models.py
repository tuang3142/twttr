import datetime
from .app import db
from marshmallow import fields, Schema

N = 128


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(N), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('users.id'),
                          nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.title = data.get('title')
        self.content = data.get('content')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        self.author_id = db.Column(db.Integer,
                                   db.ForeignKey('users.id'),
                                   nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def preview(self):
        return

    @staticmethod
    def all():
        return Blog.query.all()

    @staticmethod
    def find_by_id(id):
        return Blog.query.get(id)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(N), unique=True, nullable=False)
    fullfiled = db.Column(db.Boolean, default=False)
    blogs = db.relationship('Blog', backref='users', lazy=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def all():
        User.query.all()

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)


class BlogSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    blogs = fields.Nested(BlogSchema, many=True)
