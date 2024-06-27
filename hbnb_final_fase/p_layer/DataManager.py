#!/usr/bin/python3

from flask import jsonify
from models.IPersistenceManager import IPersistenceManager
from datetime import datetime
import json

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_lists = {
        'Users': [],
        'Reviews': [],
        'Place' : [],
        'Amenities': [],
        'Country': [],
        'City': []
        }
        try:
            with open('data_base.json', encoding="utf-8") as file:
                self.data_lists = json.load(file)
        except FileNotFoundError:
            with open('data_base.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists))

    def save(self, entity):
        class_name = entity.__class__.__name__ 
        if class_name in self.data_lists:
            self.data_lists[class_name].append(entity.__dict__)
        try:
            with open('data_base.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists, indent=4))
        except FileNotFoundError:
            return jsonify("File not found"), 404
   
    def get(self, entity_id, entity_type):
        print(entity_type)
        if type(entity_type) is not str:
            class_name = entity_type.__class__.__name__
        else:
            class_name = entity_type
            
        if class_name in self.data_lists:
            entity_list = self.data_lists[class_name]
            for entity in entity_list:
                if entity.get('id') == entity_id:
                    return entity

    def get_all(self, entity_type):
        if type(entity_type) is not str:
            class_name = entity_type.__class__.__name__
        else:
            class_name = entity_type
        if class_name in self.data_lists:
            return self.data_lists[class_name]
    
    def delete(self, entity_id, entity):
        if type(entity) is not str:
            class_name = entity.__class__.__name__
        else:
            class_name = entity
        if class_name in self.data_lists:
            entity_list = self.data_lists[class_name]
            for entity in entity_list:
                if entity.get('id') == entity_id:
                    self.data_lists[class_name].remove(entity)
            try:
                with open('data_base.json', 'w', encoding="utf-8") as file:
                    file.write(json.dumps(self.data_lists, indent=4))
            except FileNotFoundError:
                return jsonify("File not found"), 404

    def update(self, entity_id, entity, entity_type):
        if entity_type in self.data_lists:
            entity_list = self.data_lists[entity_type]
            for item in entity_list:
                if entity_id == item.get('id'):
                    item['updated_at'] = datetime.now().isoformat()
                    for key, value in entity.items():
                        item[key] = value
                    break
            try:
                with open('data_base.json', 'w', encoding="utf-8") as file:
                    file.write(json.dumps(self.data_lists, indent=4))
            except FileNotFoundError:
                return jsonify("File not found"), 404
            return item

    def get_all_country(self):
        try:
            with open('all_countries.json', encoding="utf-8") as file:
                countries = json.load(file)
        except FileNotFoundError:
                return jsonify("File not found"), 404
        return countries
    
    def get_country(self, entity_id):
        countries = DataManager.get_all_country()
        for country in countries:
            if country.get("alpha-2") == entity_id:
                return country