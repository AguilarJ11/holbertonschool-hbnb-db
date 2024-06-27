#!/usr/bin/python3

from models.basic_data import Basic_data

class Users(Basic_data):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name