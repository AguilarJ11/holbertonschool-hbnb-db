#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime
from hbnb_final_fase import db


class Basic_data:
    
    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
