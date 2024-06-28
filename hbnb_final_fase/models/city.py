#!/usr/bin/python3

from models.basic_data import Basic_data
from Run import db

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(10), db.ForeignKey('countries.code'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
