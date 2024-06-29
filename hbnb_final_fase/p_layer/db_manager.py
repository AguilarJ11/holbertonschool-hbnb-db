#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from hbnb_final_fase import db
from hbnb_final_fase.models.IPersistenceManager import IPersistenceManager
from datetime import datetime

class Db_manager(IPersistenceManager):
    def __init__(self):
        
        """
        Crea el engine para conectarse a una db especifica
        """
        engine = create_engine(
        'sqlite:///development.db',
        pool_pre_ping=True)
        
        """
        Crea todas las tablas de los modelo que fueron creados
        a partir del objeto db.
        Crea una session para hacer las consultas
        """
        db.metadata.create_all(engine)

    def save(self, entity):
        data = db.session.add(entity)
        db.session.commit()
        return data
   
    def get(self, entity_id, entity_type):
        data = db.session.get(entity_type, entity_id)
        return data

    def get_all(self, entity_type):
        data = db.session.query(entity_type).all
        return data
    
    def delete(self, entity_id, entity):
        data = db.session.query(entity).filter(entity.id==entity_id)
        db.session.delete(data)
        db.session.commit()

    def update(self, entity_id, entity, entity_type):
        data = db.session.get(entity_type, entity_id)
        data.update(entity)
        return data

    def get_all_country(self):
        pass
    
    def get_country(self, entity_id):
        pass