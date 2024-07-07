#!/usr/bin/python3

from hbnb_final_fase import db
from hbnb_final_fase.models.basic_data import Basic_data


class Amenities(Basic_data, db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())


    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }