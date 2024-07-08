#!/usr/bin/python3
"""
Module user.py
==============

This module defines the Flask blueprint for user-related routes, including 
creating, retrieving, updating, and deleting users. It uses JWT for authentication 
and authorization.

Routes:
-------
- POST /users: Creates a new user. Requires admin rights.
- GET /users: Retrieves all users.
- GET /users/<user_id>: Retrieves a specific user by user ID.
- PUT /users/<user_id>: Updates a specific user by user ID.
- DELETE /users/<user_id>: Deletes a specific user by user ID. Requires admin rights.
"""

from flask import Blueprint, request, jsonify
from hbnb_final_fase.b_logic.system import System
from hbnb_final_fase.models.users import Users
from flask_jwt_extended import jwt_required, get_jwt
user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():

    """
    Create a new user.

    Request JSON data must include 'email', 'first_name', and 'last_name'.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with the created user data and status 201 on success.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 400 on failure.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    
    data = request.get_json()
    if "@" not in data.get('email') or ".com" not in data.get('email'):
        raise ValueError("Email, not valid!")
    if not data.get('first_name'):
        raise ValueError("First Name not valid, try a new one!")
    if not data.get('last_name'):
        raise ValueError("Last Name not valid, try a new one!")
    try:
        user = System.create_user(data)
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"message":"Failed to create User.", "error": str(e)}), 400

@user_bp.route('/users', methods=['GET'])
def get_users():

    """
    Retrieve all users.

    Returns:
        JSON response with a list of all users and status 200 on success.
        JSON response with error message and status 404 if no users are found.
    """

    try:
        users = System.get_all(Users)
        return jsonify(users), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):

    """
    Retrieve a specific user by user ID.

    Args:
        user_id (UUID4): The ID of the user to retrieve.

    Returns:
        JSON response with the user data and status 200 on success.
        JSON response with error message and status 404 if user is not found.
    """

    try:
        user = System.get(user_id, Users)
        return jsonify(user), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):

    """
    Update a specific user by user ID.

    Args:
        user_id (UUID4): The ID of the user to update.
        Request JSON data must include fields to be updated.

    Returns:
        JSON response with the updated user data and status 200 on success.
        JSON response with error message and status 404 if user is not found.
    """

    data = request.get_json()
    try:
        updated = System.update(user_id, data, Users)
        return jsonify(updated), 200
    except Exception as e:
        return jsonify({"Message": "User not found", "error": str(e)}), 404


@user_bp.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):

    """
    Delete a specific user by user ID.

    Args:
        user_id (str): The ID of the user to delete.
    Requires admin rights (is_admin claim in JWT).

    Returns:
        JSON response with status 204 on successful deletion.
        JSON response with error message and status 403 if not admin.
        JSON response with error message and status 404 if user is not found.
    """

    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    
    try:
        user = System.get(user_id, Users)
        if user == None:
            return jsonify({"Message":"User not found."}), 404
        System.delete(user_id, Users)
        return jsonify({"Message":"Successfully user deleted."}), 204
    except:
        return jsonify({"Message":"User not found."}), 404
