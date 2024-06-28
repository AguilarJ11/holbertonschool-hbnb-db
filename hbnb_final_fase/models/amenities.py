#!/usr/bin/python3

import uuid
from hbnb_final_fase import db
from hbnb_final_fase.models.basic_data import Basic_data


class Amenities(db.Model, Basic_data):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name