#!/usr/bin/python3
from Run import db
# Falta agregar la creacion de tablas
class Country(db.Model):
    __tablename__ = 'countries'

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, code, name):
        self.code = code
        self.name = name