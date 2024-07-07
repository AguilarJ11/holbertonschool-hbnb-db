#!/usr/bin/python3

from hbnb_final_fase import db


class Country(db.Model):
    __tablename__ = 'countries'

    code = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, code, name):
        self.code = code
        self.name = name