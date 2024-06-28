#!/usr/bin/python3

from models.basic_data import Basic_data
from app import db


#class Users(Basic_data):
    #def __init__(self, email, first_name, last_name):
        #super().__init__()
        #self.email = email
        #self.first_name = first_name
        #self.last_name = last_name
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Asegúrate de un almacenamiento seguro
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())