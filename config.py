#!/usr/bin/python3

import os
from dotenv import load_dotenv

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