#!/usr/bin/python3

from models.basic_data import Basic_data
import uuid
from Run import db
# Falta agregar la creacion de tablas
class Amenities(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name