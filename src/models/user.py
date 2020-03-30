import datetime
from ..app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # fullfiled = boolean

    def __init__(self, data):
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<id %r>' % self.id

    @staticmethod
    def all():
        User.query.all()

    @staticmethod
    def find_by_id(id):
        return User.query.get(id)
