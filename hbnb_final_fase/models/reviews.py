#!/usr/bin/python3

from models.basic_data import Basic_data

class Reviews(Basic_data):
    def __init__(self, rating, user_id, place_id, comment):
        super().__init__()
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.comment = comment
