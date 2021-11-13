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

    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

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
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')

    def __repr__(self):
        return f'Blog {self.blog_content}'


class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text)
    blog_id = db.Column(db.Integer,db.ForeignKey('bloggs.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    def __repr__(self):
        return f'Comment : id: {self.id} comment: {self.description}'

class Subscription(db.Model):
    __tablename__='subscriptions'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    def __repr__(self):
        return f'User{self.email}'