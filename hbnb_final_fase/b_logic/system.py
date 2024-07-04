#!/usr/bin/python3

from flask import jsonify
from hbnb_final_fase.models.reviews import Reviews
from hbnb_final_fase.models.users import Users
from hbnb_final_fase.models.place import Place
from hbnb_final_fase.models.amenities import Amenities
from hbnb_final_fase.models.city import City
from config import D_manager


class System:

    def create_review(place_id, data_review):
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
                city_id = data_place.get('city_id'),
                amenity_ids = data_place.get('amenities_ids')
                )
        except Exception:
            return jsonify({"Message":"Failed to create Place."}), 400
        
        D_manager.save(new_place)
        return new_place.to_dict()

    def create_amenities(data_amenities):
        try:
            new_amenity = Amenities(
                name = data_amenities.get('name')
            )
        except Exception:
            return jsonify({"Message":"Failed to create Amenity."}), 400
        D_manager.save(new_amenity)

    def create_user(data_user):
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
            if country.get("alpha-2") == new_city.county_code:
                country_found = True
                break
        if not country_found:
            raise ValueError("Country not exist!")
        D_manager.save(new_city)
        return new_city.to_dict()

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