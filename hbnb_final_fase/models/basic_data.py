#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime
from hbnb_final_fase import db


class Basic_data:
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return "dict ;)"