from flask import Blueprint, Jsonify, session, request
import json
from app.models import User, Posts, db
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import PostForm
from app.forms import EditPostForm
from flask_login import current_user, login_user, logout_user, login_required

post_routes = Blueprint('posts', __name__)

# Get all the posts from the database
@post_routes.route('/posts')
def all_posts():
    posts = Posts.query.all()
    return {'post': [post.to_dict() for post in posts ]}

# Get a single post from the database
@post_routes.route('/posts/<int:id>/one')
def single_post(id):
    singlePost = Posts.query.filter(Posts.id == id).first()
    return {'singlePost':singlePost.to_dict()}

# Deletes a single post form the database
@post_routes.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_post(id):
    post = Posts.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return post.to_dict()