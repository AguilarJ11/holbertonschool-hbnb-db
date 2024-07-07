#!/usr/bin/python3

from hbnb_final_fase import db
from hbnb_final_fase.models.IPersistenceManager import IPersistenceManager
from hbnb_final_fase.models.country import Country
from datetime import datetime

"""
Modulo de persistencia en una base de datos.
"""


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
        data = db.session.get(entity, entity_id)
        db.session.delete(data)
        db.session.commit()

    def update(self, entity_id, entity, entity_type):
        entity['updated_at'] = datetime.now()
        db.session.query(entity_type).filter(entity_type.id == entity_id).update(entity)
        db.session.commit()
        updated = db.session.get(entity_type, entity_id)
        return updated.to_dict()

    def get_all_country(self):
        data = db.session.query(Country).all()
        data_list = []
        for entity in data:
            data_list.append(entity.to_dict())
        return data_list
    
    def get_country(self, entity_id):
        data = db.session.get(Country, entity_id)
        return data.to_dict()