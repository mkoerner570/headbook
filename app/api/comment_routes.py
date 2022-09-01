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

# Get a single Comment from the database
@comment_routes.route('/comments/<int:id>/single')
def single_comment(id):
    singleComment = Comments.query.filter(Comments.id == id).first()
    return {'singleComment':singleComment.to_dict()}

# Deletes a single Comment from the database
@comment_routes.route('/delete/<int:id>/',methods=['DELETE'])
@login_required
def delete_comment(id):
    comment = Comments.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return comment.to_dict()
