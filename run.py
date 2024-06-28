#!/usr/bin/python3

from flask import Flask
from hbnb_final_fase import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)