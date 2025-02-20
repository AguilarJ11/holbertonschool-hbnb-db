#!/usr/bin/python3

from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
       @abstractmethod
       def save(self, entity):
           pass

       @abstractmethod
       def get(self, entity_id, entity_type):
           pass
       
       @abstractmethod
       def get_all(self, entity_type):
           pass

       @abstractmethod
       def update(self, entity_id, entity, entity_type):
           pass

       @abstractmethod
       def delete(self, entity_id, entity_type):
           pass
       
       @abstractmethod
       def get_country(self, entity_id):
           pass
       
       @abstractmethod
       def get_all_country(self):
           pass