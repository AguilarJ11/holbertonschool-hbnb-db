#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System

amenity_bp = Blueprint('amenity', __name__)


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    try:
        amenity = System.create_amenities(data)
        return jsonify(amenity), 201
    except Exception as e:
        return jsonify({f"Message":"An error creating an Amenity {e}"}), 404

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    try:
        amenity = System.get_all('Amenities')
        return jsonify(amenity), 200
    except:
        return jsonify({"Message":"Amenity not found."}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    try:
        amenity = System.get(amenity_id, 'Amenities')
        return jsonify(amenity), 200
    except:
        return jsonify({"Message":"User not found."}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    try:
        updated = System.update(amenity_id, data, 'Amenities')
        return jsonify(updated), 200
    except:
        return jsonify({"Message": "User not found"}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        amenity = System.get(amenity_id, 'Amenities')
        if amenity == None:
            return jsonify({"Message":"Amenity not found."}), 404
        System.delete(amenity_id, 'Amenities')
        return jsonify({"Message":"Deleted amenity succesfully."}), 204
    except:
        return jsonify({"Message":"Amenity not found."}), 404