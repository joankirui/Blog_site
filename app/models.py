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

class Blog(db.Model):
    __tablename__='bloggs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String(255),index=True)
    author = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    posted_on = db.Column(db.DateTime, default = datetime.utcnow().strftime('%d %b %Y'))
    # relationships will relate to the comment model


class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text)
    blog_id = db.Column(db.Integer,db.ForeignKey('bloggs.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)