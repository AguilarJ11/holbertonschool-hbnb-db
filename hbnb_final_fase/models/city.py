#!/usr/bin/python3

from hbnb_final_fase.models.basic_data import Basic_data
from hbnb_final_fase import db


class City(Basic_data, db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(2), db.ForeignKey('countries.code'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())


    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }