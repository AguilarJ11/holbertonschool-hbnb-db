#!/usr/bin/python3

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from blueprints.user import user_bp
from blueprints.countries_and_cities import country_bp
from blueprints.place import place_bp
from blueprints.review import review_bp
from blueprints.amenity import amenity_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(user_bp)
app.register_blueprint(country_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(amenity_bp)

if __name__ == "__main__":
    app.run(debug=True)