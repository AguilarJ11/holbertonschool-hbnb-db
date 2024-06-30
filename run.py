#!/usr/bin/python3

from flask import Flask
from hbnb_final_fase import create_app, db


app = create_app()
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)