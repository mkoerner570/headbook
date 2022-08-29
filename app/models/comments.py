from .db import db

class Comments(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.TextArea)
    pic = db.Column(db.String)
    likes = db.Column(db.Interger)

    user_id = db.Column(db.Interger, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="comments")

    post_id = db.Column(db.Interger, db.ForeignKey("posts.id"))
    posts = db.relationship("Posts", back_populates="comments")

