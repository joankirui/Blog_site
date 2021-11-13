from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Quotes:
    def __init__(self,author,id,quote):
        self.id = id
        self.author = author
        self.quote = quote

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # relationships
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

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

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.filter_by(blog_id = id).desc().all()
        return blogs
        
    def __repr__(self):
        return f'Blog {self.blog_content}'


class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text)
    blog_id = db.Column(db.Integer,db.ForeignKey('bloggs.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment : id: {self.id} comment: {self.description}'

class Subscription(db.Model):
    __tablename__='subscriptions'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def __repr__(self):
        return f'User{self.email}'