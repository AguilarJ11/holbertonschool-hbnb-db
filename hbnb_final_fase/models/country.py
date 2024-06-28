#!/usr/bin/python3
from app import db

class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name