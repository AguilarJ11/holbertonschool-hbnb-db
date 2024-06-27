#!/usr/bin/python3

from models.basic_data import Basic_data

class City(Basic_data):
    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.county_code = country_code
