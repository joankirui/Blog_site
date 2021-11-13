from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment,Subscription


@main.route('/',methods = ['GET','POST'])
def index():
    blog = Blog.query.all()
    title = "Welcome to Blogsite"
    # Getting the quotes
    # quotes = get_quotes

@main.route('/new/blog/', methods=['GET','POST'])
@login_required
def new_blog():







@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

