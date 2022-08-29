from .db import db

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.String)