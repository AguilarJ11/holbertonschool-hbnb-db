#!/usr/bin/python3

from models.basic_data import Basic_data
from Run import db
# Falta agregar la creacion de tablas
class Reviews(db.Model):# Si es multimple herencia no duplicamos codigo
    __tablename__ = 'reviews' 

    id = db.Column(db.String(36), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.String(36), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, rating, user_id, place_id, comment):
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.comment = comment
