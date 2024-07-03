#!/usr/bin/python3
from hbnb_final_fase import db


class Amenities_places(db.Model):
    __tablename__ = 'amenities_places'

    place_id = db.Column(db.String(36), primary_key=True)
    amenities_id = db.Column(db.String(36), primary_key=True)

    def __init__(self, place_id, amenities_id):
        self.place_id = place_id
        self.amenities_id = amenities_id
