from flask import Blueprint, jsonify, session, request
from app.models import User, Comments, Posts,db
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import CommentForm, EditCommentForm
from flask_login import current_user, login_user, logot_user,login_required

comment_routes = Blueprint('comments', __name__)

