from flask_wtf import FlaskForm 
from wtforms import SelectField,StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class NewBlog(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    blog_content = TextAreaField('Blog to post',validators=[Required()])
    author = StringField('Author',validators=[Required()])
    submit = SubmitField('submit')

class MyComment(FlaskForm):
    description = TextAreaField('Tell us what you think',validators=[Required()])
    submit = SubmitField('submit')

class UpdateBlog(FlaskForm):
    updates = TextAreaField('update your blog',validators=[Required()])
    submit = SubmitField('submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()])
    submit = SubmitField('submit')