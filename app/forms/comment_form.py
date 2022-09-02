from flask_wtf import FlaskForm
from wtforms import TextAreaField, Integerfield, SubmitField, FileField, HiddenField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class CommentForm(FlaskForm):
    post_id=HiddenField("post_id")
    content=TextAreaField("content")
    location=StringField("location")
    submit=SubmitField("Submit")

class EditCommentForm(FlaskForm):
    post_id=HiddenField("post_id")
    content=TextAreaField("content")
    location=StringField("location")
    submit=SubmitField("Submit")