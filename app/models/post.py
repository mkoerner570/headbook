from .db import db

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.String)
    pic = db.Column(db.String)
    likes = db.Column(db.Interger)

    user_id = db.Column(db.Interger, db.ForeignKey('users.id'))
    users. db.relationship("User", back_populates="posts")
    comments = db.relationship("Comments", back_populates="posts", cascade="all, delete")

    def to_dict(self):
        return{
            "id":self.id,
            "body":self.body,
            "pic":self.pic,
            "likes":self.likes,
            "user_id":self.user_id,
        }