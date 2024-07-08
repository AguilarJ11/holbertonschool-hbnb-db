#!/usr/bin/python3

"""
Module place.py
===============

This module defines the Flask blueprint for place-related routes, including 
creating, retrieving, updating, and deleting places. It uses JWT for authentication 
and authorization.

Routes:
-------
- POST /places: Creates a new place. Requires admin rights.
- GET /places: Retrieves all places.
- GET /places/<place_id>: Retrieves a specific place by place ID.
- PUT /places/<place_id>: Updates a specific place by place ID. Requires admin rights.
- DELETE /places/<place_id>: Deletes a specific place by place ID. Requires admin rights.
"""

from flask import Blueprint, request, jsonify
from hbnb_final_fase.b_logic.system import System
from hbnb_final_fase.models.amenities import Amenities
from hbnb_final_fase.models.place import Place
from flask_jwt_extended import jwt_required, get_jwt

place_bp = Blueprint('place', __name__)

@place_bp.route('/places', methods=['POST'])
@jwt_required()
def create_place():

    """
    Create a new place.

    Request JSON data must include 'description', 'rooms', 'bathrooms', 'max_guests', 
    'price_per_night', 'latitude', and 'longitude'. Amenity IDs must be valid.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with the created place data and status 200 on success.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 400 on failure.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    
    data = request.get_json()
    amenities = System.get_all(Amenities)
    
    for amenity_id in data.get('amenity_ids', []):
        amenity_found = False
        for amenity in amenities:
            if not isinstance(amenity, dict):
                amenity = amenity.to_dict()
            if amenity.get("id") == amenity_id:
                amenity_found = True
                break
        if not amenity_found:
            raise ValueError("Amenity not found!")
    if data.get('description') == "":
        raise TypeError("The place must have a description!")
    if not data.get('rooms') or data.get('rooms') <= 0:
        raise ValueError("The place must have at least one room!")
    if not data.get('bathrooms') or data.get('bathrooms') <= 0:
        raise ValueError("The place must have at least one bathroom!")
    if not data.get('max_guests') or data.get('max_guests') <= 0:
        raise ValueError("The place must have at least one guest!")
    if not data.get('price_per_night') or data.get('price_per_night') <= 0:
        raise ValueError("Price per night must be positive!")
    if not data.get('latitude') or not -90 <= data.get('latitude') <= 90:
        raise ValueError("Please enter a latitud between -90 and 90")
    if not data.get('longitude') or not -180 <= data.get('longitude') <= 180:
        raise ValueError("Please enter a longitude between -180 and 180")
    try:
        place = System.create_place(data)
        return jsonify(place), 200
    except Exception as e:
        return jsonify({"Message":"An error creating a place {}".format(e)}), 400


@place_bp.route('/places', methods=['GET'])
def get_places():

    """
    Retrieve all places.

    Returns:
        JSON response with a list of all places and status 200 on success.
        JSON response with error message and status 404 if no places are found.
    """

    try:
        place = System.get_all(Place)
        return jsonify(place), 200
    except:
        return jsonify({"Message":"Places not found."}), 404
    
@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):

    """
    Retrieve a specific place by place ID.

    Args:
        place_id (UUID4): The ID of the place to retrieve.

    Returns:
        JSON response with the place data and status 200 on success.
        JSON response with error message and status 404 if place is not found.
    """

    try:
        place = System.get(place_id, Place)
        return jsonify(place), 200
    except:
        return jsonify({"Message":"Place not found."}), 404

@place_bp.route('/places/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):

    """
    Update a specific place by place ID.

    Args:
        place_id (UUID4): The ID of the place to update.
        Request JSON data must include fields to be updated.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with the updated place data and status 200 on success.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 404 on failure.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    data = request.get_json()
    try:
        u_place = System.update(place_id, data, Place)
        return jsonify(u_place), 200
    except:
        return jsonify({"Message": "Place not found"}), 404

@place_bp.route('/places/<place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    
    """
    Delete a specific place by place ID.

    Args:
        place_id (UUID4): The ID of the place to delete.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with status 204 on successful deletion.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 404 if place is not found.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    
    try:
        place = System.get(place_id, Place)
        if place == None:
            return jsonify({"Message":"Place not found."}), 404
        System.delete(place_id, 'Place')
        return jsonify({"Message":"Successfully place deleted."}), 204
    except:
        return jsonify({"Message":"Place not found."}), 404
