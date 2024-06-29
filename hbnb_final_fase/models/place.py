#!/usr/bin/python3

from hbnb_final_fase.models.basic_data import Basic_data
from hbnb_final_fase import db


class Place(Basic_data, db.Model):
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True)
    host_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.String(40), db.ForeignKey('cities.id'), nullable=False)
    amenity_id = db.Column(db.String(40), db.ForeignKey('amenities.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, host_id, name, description, rooms, bathrooms,\
                max_guests, price_per_night, latitude, longitude, city_id, amenity_ids):
        super().__init__()
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

    def to_dict(self):
        return {
            "id": self.id,
            "host_id": self.host_id,
            "name": self.name,
            "description": self.description,
            "rooms": self.rooms,
            "bathrooms": self.bathrooms,
            "max_guests": self.max_guests,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "amenity_ids": self.amenity_ids,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

