#!/usr/bin/python3

"""
Modulo utilizado para el alta, baja y control de
entidades.
"""



from flask import jsonify
from hbnb_final_fase.models.reviews import Reviews
from hbnb_final_fase.models.users import Users
from hbnb_final_fase.models.place import Place
from hbnb_final_fase.models.amenities import Amenities
from hbnb_final_fase.models.city import City
from hbnb_final_fase.models.amenities_places import Amenities_places
from config import D_manager, persistence


class System:
    
    """
    Clase que gestiona la creacion y modificacion de entidades.
    """

    def create_review(place_id, data_review):
        
        """
        Crea una nueva review para un lugar.

        Parámetros:
        place_id (str): ID del lugar.
        data_review (dict): Datos de la review ('user_id', 'comment', 'rating').

        Retorno:
        dict o tuple: La review creada o un mensaje de error con el código de estado HTTP 400.

        Excepciones:
        Errors: Si el usuario hace una review de su propio lugar o ya hizo una review del lugar.
        """
        
        
        try:
            new_review = Reviews(
                user_id = data_review.get('user_id'),
                place_id = place_id,
                comment = data_review.get('comment'),
                rating = data_review.get('rating')
            )
        except Exception:
            return jsonify({"Message":"Failed to create review."}), 400
        place = D_manager.get(place_id, Place)
        if place and place.get('host_id') == new_review.user_id:
            raise ValueError("User cannot review their own place")
        existing_review = D_manager.get_all(new_review.__class__)
        for review in existing_review:
            if not new_review.user_id in review.get('user_id'):
                raise ValueError("User not found!")
            if new_review.user_id in review.get('id') and place_id in review.get('place_id'):
                raise ValueError("User cannot review multiple times on the same place")
        existing_place = D_manager.get_all(Place)
        for place in existing_place:
            if not new_review.place_id in place.get('id'):
                raise ValueError("Place not found!")

        D_manager.save(new_review)
        return new_review.to_dict()
    
    def create_place(data_place):
        """
        Crea un nuevo lugar.

        Parámetros:
        data_place (dict): Datos del lugar 
            ('name', 'host_id', 'description', 'rooms', 
            'bathrooms', 'max_guests', 'price_per_night', 'latitude', 
            'longitude', 'city_id', 'amenities_ids').

        Retorno:
        dict o tuple: El lugar creado o un mensaje de error con el código de estado HTTP 400.
        """
        try:
            new_place = Place(
                name = data_place.get('name'),
                host_id = data_place.get('host_id'),
                description = data_place.get('description'),
                rooms = data_place.get('rooms'),
                bathrooms = int(data_place.get('bathrooms')),
                max_guests = int(data_place.get('max_guests')),
                price_per_night = float(data_place.get('price_per_night')),
                latitude = float(data_place.get('latitude')),
                longitude = float(data_place.get('longitude')),
                city_id = data_place.get('city_id')
                )
        except Exception:
            return jsonify({"Message":"Failed to create Place."}), 400
        
        """
        Dependiendo el tipo de persistencia, como se guarda la info
        de las amenities que tiene el place recientemente inicializado.
        """
        
        if persistence != 'db':
            new_place.amenity_ids = data_place.get('amenities_ids')
        else:
            for amen in data_place.get('amenities_ids', []):
                amenities_places = Amenities_places (
                    place_id = new_place.id,
                    amenities_id = amen
                )
                D_manager.save(amenities_places)

        D_manager.save(new_place)
        return new_place.to_dict()

    def create_amenities(data_amenities):
        
        """
        Crea una nueva 'amenity'.

        Parámetros:
        data_amenities (dict): Datos('name').

        Retorno:
        dict o tuple: La 'amenity' creada o un mensaje de error con el código de estado HTTP 400.
        """

        try:
            new_amenity = Amenities(
                name = data_amenities.get('name')
            )
        except Exception:
            return jsonify({"Message":"Failed to create Amenity."}), 400
        D_manager.save(new_amenity)

    def create_user(data_user):
        
        """
        Crea un nuevo usuario.

        Parámetros:
        data_user (dict): Datos del usuario ('email', 'password', 'first_name', 'last_name').

        Retorno:
        dict o tuple: El usuario creado o un mensaje de error con el código de estado HTTP 400.

        Excepciones:
        ValueError: Si el email ya existe.
        """
        
        try:
            new_user = Users(
                email = data_user.get('email'),
                password = data_user.get('password'),
                first_name = data_user.get('first_name'),
                last_name = data_user.get('last_name')
            )
        except Exception:
            return jsonify({"Message":"Failed to create User."}), 400

        existing_users = D_manager.get_all(new_user.__class__)
        for user in existing_users:
            if isinstance(user, dict):
                if user.get('email') == data_user.get('email'):
                    raise ValueError("Email already exist!")
            else:
                if user.email == data_user.get('email'):
                    raise ValueError("Email already exist!")

        D_manager.save(new_user)
        return new_user.to_dict()

    def create_city(data_city):
        
        """
        Crea una nueva ciudad.

        Parámetros:
        data_city (dict): Datos de la ciudad ('name', 'country_code').

        Retorno:
        dict o tuple: La ciudad creada o un mensaje de error con el código de estado HTTP 400.

        Excepciones:
        ValueError: Si el código de país no existe.
        """
        
        try:
            new_city = City(
                name = data_city.get('name'),
                country_code = data_city.get('country_code')
            )
        except Exception:
            return jsonify({"Message":"Failed to create City."}), 400

        countries = D_manager.get_all_country()
        for country in countries:
            country_found = False
            if persistence != 'db':
                if country.get("alpha-2") == new_city.county_code:
                    country_found = True
                    break
            else:
                if country.code == new_city.country_code:
                    country_found = True
        if not country_found:
            raise ValueError("Country not exist!")

        D_manager.save(new_city)
        return new_city.to_dict()


    """
    Metodos que conectan capa de servicios con
    capa de persistencia.
    """

    def update(entity_id, entity, entity_type):
       return D_manager.update(entity_id, entity, entity_type)
    
    def delete(entity_id, entity_type): 
        D_manager.get(entity_id, entity_type)
        D_manager.delete(entity_id, entity_type)
    
    def get(entity_id, entity_type):
        return D_manager.get(entity_id, entity_type)
    
    def get_all(entity_type):
        return D_manager.get_all(entity_type)
    
    def get_all_countries():
        return D_manager.get_all_country()
    
    def get_country(entity_id):
        return D_manager.get_country(entity_id)