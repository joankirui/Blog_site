from flask_login import login_required,current_user
from flask_wtf import form
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment,Subscription
from .forms import UpdateBlog,UpdateProfile,NewBlog,MyComment,SubscribeForm
from .. import db

@main.route('/',methods = ['GET','POST'])
def index():
    blog = Blog.query.all()
    title = "Welcome to Blogsite"
    # Getting the quotes
    # quotes = get_quotes

    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        subscription = Subscription(email = email)
        db.session.add(subscription)
        db.session.commit()
        return render_template('index.html',title = title,blog = blog)
    return render_template('index.html',title = title,blog = blog)
@main.route('/new/blog/', methods=['GET','POST'])
@login_required
def new_blog():







@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

