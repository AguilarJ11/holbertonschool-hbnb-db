#!/usr/bin/python3

from models.basic_data import Basic_data
from Run import db

class Place(db.Model): # Si es multiple heredable usamos basic data sino no
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True)
    host_id = db.Column(db.String(36), db.Foreing_Key('user.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.String(40), db.Foreing_Key('city.id'), nullable=False)
    amenity_id = db.Column(db.String(40), db.Foreing_Key('amenity.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, host_id, name, description, rooms, bathrooms,\
                max_guests, price_per_night, latitude, longitude, city_id, amenity_ids):
        self.host_id = host_id
        self.name = name
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_ids = amenity_ids


