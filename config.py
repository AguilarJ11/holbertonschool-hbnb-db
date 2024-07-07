#!/usr/bin/python3

import os
from dotenv import load_dotenv
import pycountry

"""
Este modulo importa y configura el tipo de persistencia con la que vamos a trabajar
previamente seteado en el .env
"""


load_dotenv('app.env')
persistence = os.getenv('PERSISTENCE')
database_type = os.getenv('DATABASE_TYPE')
database_url = os.getenv('DATABASE_URL')
env_name = os.getenv('ENV')

if persistence == 'db':
    
    from hbnb_final_fase.p_layer.db_manager import Db_manager
    
    print(f"{database_type} db persistence")
    D_manager = Db_manager()

elif persistence == 'file':
    
    from hbnb_final_fase.p_layer.dataManager import DataManager

    print(f"{persistence} persistence")
    D_manager = DataManager()   

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


"""
Modulo utilizado solamente con persistencia en db

Crea las tablas de la base de datos, crea un registro
de paises para la tabla countries y crea un usuario admin
"""

def create_db(app, db):
    
   with app.app_context():
    db.create_all()

    from hbnb_final_fase.models.country import Country
    from hbnb_final_fase.models.users import Users

    try:
        
        admin = Users(
            email = "admin@full_chad",
            is_admin = 1,
            password = "123",
            first_name = "el_",
            last_name = "admin",
        )
        D_manager.save(admin)
        
        for countrie in pycountry.countries:
            new_country = Country (
                name = countrie.name,
                code = countrie.alpha_2,
            )
            D_manager.save(new_country)
        
    except Exception as e:
        pass