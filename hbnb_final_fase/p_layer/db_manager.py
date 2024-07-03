#!/usr/bin/python3

from sqlalchemy import create_engine
from hbnb_final_fase import db
from hbnb_final_fase.models.IPersistenceManager import IPersistenceManager
from datetime import datetime

class Db_manager(IPersistenceManager):
    
    def save(self, entity):
        data = db.session.add(entity)
        db.session.commit()
        return data
   
    def get(self, entity_id, entity_type):
        data = db.session.get(entity_type, entity_id)
        return data.to_dict()

    def get_all(self, entity_type):
        data = db.session.query(entity_type).all()
        data_list = []
        for entity in data:
            data_list.append(entity.to_dict())
        return data_list
    
    def delete(self, entity_id, entity):
        data = db.session.query(entity).filter(entity.id==entity_id)
        db.session.delete(data)
        db.session.commit()

    def update(self, entity_id, entity, entity_type):
        data = db.session.get(entity_type, entity_id)
        data.update(entity)
        return data.to_dict()

    def get_all_country(self):
        pass
    
    def get_country(self, entity_id):
        pass