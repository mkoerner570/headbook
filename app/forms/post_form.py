from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField, FileField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class PostForm(FlaskForm):
    image=FileField("image")
    body=TextAreaField("body")
    submit=SubmitField("Submit")

class EditPostForm(FlaskForm):
    body=TextAreaField("body")
    submit=SubmitField("Submit")