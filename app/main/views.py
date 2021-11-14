from flask_login import login_required,current_user
from ..requests import get_quotes
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment,Subscription
from .forms import UpdateBlog,UpdateProfile,NewBlog,MyComment,SubscribeForm
from .. import db,photos

@main.route('/',methods = ['GET','POST'])
def index():
    blog = Blog.query.all()
    title = "Welcome to Blogsite"
    # Getting the quotes
    quotes = get_quotes()
    print(quotes)

    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        subscription = Subscription(email = email)
        db.session.add(subscription)
        db.session.commit()
        return render_template('index.html',title = title,blog = blog,quotes = quotes)
    return render_template('index.html',title = title,blog = blog,quotes = quotes)

@main.route('/new/blog/', methods=['GET','POST'])
@login_required
def new_blog():
    form = NewBlog()
    if form.validate_on_submit():
        title = form.title.data
        blog_content = form.blog_content.data
        owner_id = current_user
        print(current_user._get_current_object().id)

        new_blog = Blog(owner_id=current_user._get_current_object().id,title = title,blog_content = blog_content)

        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('blogs.html',form = form)

@main.route('/new/comment/<int:blog_id>',methods=['GET','POST'])
@login_required
def new_comment(blog_id):
    form = MyComment()
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(description = description,user_id=current_user._get_current_object().id, blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment',form = form,blog_id=blog_id))
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html',form = form,comments = all_comments)

@main.route('/deleteComment/<int:comment_id>/<int:blog_id>', methods = ["GET","POST"])
def delete_Comment(comment_id,blog_id):
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.new_blog", id = blog_id))

@main.route('/deleteblog/<int:blog_id>', methods=["GET", "POST"])  
def delete_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    uname = current_user.username
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("main.profile", uname = uname))

@main.route('/updateblog/<int:blog_id>', methods=["GET", "POST"])
def edit_blog(blog_id):
    form = UpdateBlog()
    if form.validate_on_submit():
        updates = form.updates.data
        blog = Blog.query.filter_by(id = blog_id).updates({"updates":updates})
        db.session.commit()
        return redirect(url_for("main.profile", uname = current_user.username))
    else:
        form.updates.data = Blog.query.filter_by(id = blog_id).first()
    return render_template("update-blog.html",updateblog_form = form)
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



