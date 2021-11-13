from . import db

class Quotes:
    def __init__(self,author,id,quote):
        self.id = id
        self.author = author
        self.quote = quote

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    # relationships

    def __repr__(self):
        return f'User {self.username}'