import datetime
from .app import db

N = 128


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(N), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # fullfiled = boolean

    def __init__(self, data):
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def __repr__(self):
        return '<id %r>' % self.id

    @staticmethod
    def all():
        User.query.all()

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)


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

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self, data):
    #     for key, item in data.items():
    #         setattr(self, key, item)
    #     self.updated_at = datetime.datetime.utcnow()
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # def preview(self):
    #     return

    @staticmethod
    def all():
        return Blog.query.all()

    @staticmethod
    def find_by_id(id):
        return Blog.query.get(id)

    def __repr__(self):
        return '<id: {}>'.format(self.id)
