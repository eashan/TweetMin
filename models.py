from app import db,bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class blogpost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, description,authorid):
        #self.title = title
        self.description = description
        self.author_id=authorid

    def __repr__(self):
        return '<description {}'.format(self.description)


class user(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = relationship("blogpost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}>'.format(self.name)