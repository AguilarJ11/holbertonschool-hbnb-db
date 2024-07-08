#!/usr/bin/python3

"""
Module amenity.py
=================

This module defines the Flask blueprint for amenity-related routes, including 
creating, retrieving, updating, and deleting amenities. It uses JWT for 
authentication and authorization.

Routes:
-------
- POST /amenities: Creates a new amenity. Requires admin rights.
- GET /amenities: Retrieves all amenities.
- GET /amenities/<amenity_id>: Retrieves a specific amenity by amenity ID.
- PUT /amenities/<amenity_id>: Updates a specific amenity by amenity ID.
- DELETE /amenities/<amenity_id>: Deletes a specific amenity by amenity ID. Requires admin rights.
"""

from flask import Blueprint, request, jsonify
from hbnb_final_fase.b_logic.system import System
from hbnb_final_fase.models.amenities import Amenities
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

amenity_bp = Blueprint('amenity', __name__)

@amenity_bp.route('/amenities', methods=['POST'])
@jwt_required()
def create_amenity():

    """
    Create a new amenity.

    Request JSON data must include necessary fields for creating an amenity.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with the created amenity data and status 201 on success.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 404 on failure.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    
    data = request.get_json()
    try:
        amenity = System.create_amenities(data)
        return jsonify(amenity), 201
    except Exception as e:
        return jsonify({f"Message":"An error creating an Amenity {e}"}), 404

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():

    """
    Retrieve all amenities.

    Returns:
        JSON response with a list of all amenities and status 200 on success.
        JSON response with error message and status 404 if no amenities are found.
    """

    try:
        amenity = System.get_all(Amenities)
        return jsonify(amenity), 200
    except:
        return jsonify({"Message":"Amenity not found."}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):

    """
    Retrieve a specific amenity by amenity ID.

    Args:
        amenity_id (UUID4): The ID of the amenity to retrieve.

    Returns:
        JSON response with the amenity data and status 200 on success.
        JSON response with error message and status 404 if amenity is not found.
    """

    try:
        amenity = System.get(amenity_id, Amenities)
        return jsonify(amenity), 200
    except:
        return jsonify({"Message":"User not found."}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):

    """
    Update a specific amenity by amenity ID.

    Args:
        amenity_id (UUID4): The ID of the amenity to update.
        Request JSON data must include fields to be updated.

    Returns:
        JSON response with the updated amenity data and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    data = request.get_json()
    try:
        updated = System.update(amenity_id, data, Amenities)
        return jsonify(updated), 200
    except:
        return jsonify({"Message": "User not found"}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
@jwt_required()
def delete_amenity(amenity_id):

    """
    Delete a specific amenity by amenity ID.

    Args:
        amenity_id (str): The ID of the amenity to delete.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with status 204 on successful deletion.
        JSON response with error message and status 403 if not admin.
        JSON 
    """
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    try:
        amenity = System.get(amenity_id, Amenities)
        if amenity == None:
            return jsonify({"Message":"Amenity not found."}), 404
        System.delete(amenity_id, Amenities)
        return jsonify({"Message":"Deleted amenity succesfully."}), 204
    except:
        return jsonify({"Message":"Amenity not found."}), 404