from flask import Blueprint, jsonify, session, request
from app.models import User, Comments, Posts,db
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import CommentForm, EditCommentForm
from flask_login import current_user, login_user, logot_user,login_required

comment_routes = Blueprint('comments', __name__)

# Get all Comments from the database
@comment_routes.route('/posts/<int:id>/comments')
def get_comments(id):
    post_comments = Comments.query.filter(Comments.post_id == id).all()
    return {'allComments':[comment.to_dict() for comment in post_comments]}

