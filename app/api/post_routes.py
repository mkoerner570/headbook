from flask import Blueprint, Jsonify, session, request
import json
from app.models import User, Post, db
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import PostForm
from app.forms import EditPostForm
from flask_login import current_user, login_user, logout_user, login_required

post_routes = Blueprint('posts', __name__)

@post_routes.route('/posts')
def all_posts():
    posts = Post.query.all()
    return {'post': [post.to_dict() for post in posts]}