#!/usr/bin/python3

from hbnb_final_fase.models.basic_data import Basic_data
from hbnb_final_fase import db


class Reviews(db.Model, Basic_data):
    __tablename__ = 'reviews' 

    id = db.Column(db.String(36), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, rating, user_id, place_id, comment):
        super().__init__()
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.comment = comment
