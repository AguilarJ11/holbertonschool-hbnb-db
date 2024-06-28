#!/usr/bin/python3

from hbnb_final_fase.models.basic_data import Basic_data
from hbnb_final_fase import db


class City(db.Model, Basic_data):
    __tablename__ = 'cities'

    name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(2), db.ForeignKey('countries.code'), nullable=False)

    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code
