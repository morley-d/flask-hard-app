from setup_db import db


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String)
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer)