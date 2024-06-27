#!/usr/bin/python3

from models.basic_data import Basic_data
import uuid

class Amenities:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
