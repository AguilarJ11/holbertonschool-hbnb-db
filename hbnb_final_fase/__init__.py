#!/usr/bin/python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from sqlalchemy import create_engine


db = SQLAlchemy()


def create_app():
    
    """
    Crea la app de flask, registra rutas y
    configura para conectarse a la db
    """
    app = Flask(__name__)
    
    #app.config.from_object(config_by_name[env_name])
    
    app.config['JWT_SECRET_KEY'] = 'super-secret-holberton'  # key
    register_routes(app)
    db_config(app)
    jwt = JWTManager(app)
    return app


def register_routes(app):
    
    """
    Registra rutas en la app
    """
    from hbnb_final_fase.blueprints.user import user_bp
    from hbnb_final_fase.blueprints.countries_and_cities import country_bp
    from hbnb_final_fase.blueprints.place import place_bp
    from hbnb_final_fase.blueprints.review import review_bp
    from hbnb_final_fase.blueprints.amenity import amenity_bp
    from hbnb_final_fase.blueprints.login import login_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(place_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(login_bp)

def db_config(app):
    
    from hbnb_final_fase.p_layer import database_url
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    db.init_app(app)
