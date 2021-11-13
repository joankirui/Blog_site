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
    