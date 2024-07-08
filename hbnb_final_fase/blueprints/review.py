#!/usr/bin/python3                                                                                                                                                                                                                                                           

"""
Module review.py
================

This module defines the Flask blueprint for review-related routes, including 
creating, retrieving, updating, and deleting reviews for places and users.

Routes:
-------
- POST /places/<place_id>/reviews: Creates a new review for a place.
- GET /users/<user_id>/reviews: Retrieves all reviews made by a user.
- GET /place/<place_id>/reviews: Retrieves all reviews for a specific place.
- GET /review/<review_id>: Retrieves a specific review by review ID.
- PUT /review/<review_id>: Updates a specific review by review ID.
- DELETE /review/<review_id>: Deletes a specific review by review ID.
"""

from flask import Blueprint, request, jsonify
from hbnb_final_fase.b_logic.system import System
from hbnb_final_fase.models.reviews import Reviews

review_bp = Blueprint('review', __name__)


@review_bp.route('/places/<place_id>/reviews', methods=['POST'])

def create_place_review(place_id):

    """
    Create a new review for a place.

    Args:
        place_id (UUID4): The ID of the place to review.
        Request JSON data must include 'rating' and 'comment'.

    Returns:
        JSON response with the created review data and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    data = request.get_json()
    if data.get('rating') <= 0 or data.get('rating') > 5:
        raise ValueError("Rating must be a number from 1 to 5")
    if not data.get('rating'):
        raise ValueError("Rating must be setted!")
    if not data.get('comment'):
        raise ValueError("Must write a coment!")
    if not place_id:
        raise ValueError("Must enter a place id")
    try:
        review = System.create_review(place_id, data)
        return jsonify(review), 200
    except Exception as e:
        return jsonify({f"Message":"An error creating a review {e}"}), 404

@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_review(user_id):

    """
    Retrieve all reviews made by a specific user.

    Args:
        user_id (UUID4): The ID of the user whose reviews to retrieve.

    Returns:
        JSON response with a list of reviews and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    try:
        all_reviews = System.get_all(Reviews)
        reviews = []
        for review in all_reviews:
            if review['user_id'] == user_id:
                reviews.append(review)
        return jsonify(reviews), 200
    except Exception as e:
        return jsonify({"Message":f"User not found.{e}"}), 404

@review_bp.route('/place/<place_id>/reviews', methods=['GET'])
def get_place_review(place_id):

    """
    Retrieve all reviews for a specific place.

    Args:
        place_id (UUID4): The ID of the place whose reviews to retrieve.

    Returns:
        JSON response with a list of reviews and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    try:
        all_reviews = System.get_all(Reviews)
        reviews = []
        for review in all_reviews:
            if review['place_id'] == place_id:
                reviews.append(review)
        return jsonify(reviews), 200
    except Exception as e:
        return jsonify({"Message":f"User not found. {e}"}), 404

@review_bp.route('/review/<review_id>', methods=['GET'])
def get_review(review_id):

    """
    Retrieve a specific review by review ID.

    Args:
        review_id (str): The ID of the review to retrieve.

    Returns:
        JSON response with the review data and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    try:
        all_reviews = System.get_all(Reviews)
        reviews = []
        for review in all_reviews:
            if review['id'] == review_id:
                reviews.append(review)
        return jsonify(review), 200
    except Exception as e:
        return jsonify({"Message":f"Review not found. {e}"}), 404

@review_bp.route('/review/<review_id>', methods=['PUT'])
def update_review(review_id):

    """
    Update a specific review by review ID.

    Args:
        review_id (UUID4): The ID of the review to update.
        Request JSON data must include fields to be updated.

    Returns:
        JSON response with the updated review data and status 200 on success.
        JSON response with error message and status 404 on failure.
    """

    data = request.get_json()
    try:
        review = System.update(review_id, data, Reviews)
        return jsonify(review), 200
    except:
        return jsonify({"Message": "Review not found"}), 404

@review_bp.route('/review/<review_id>', methods=['DELETE'])
def delete_review(review_id):

    """
    Delete a specific review by review ID.

    Args:
        review_id (UUID4): The ID of the review to delete.

    Returns:
        JSON response with status 204 on successful deletion.
        JSON response with error message and status 404 if review is not found.
    """

    try:
        review = System.get(review_id, Reviews)
        if review == None:
            return jsonify({"Message":"Review not found."}), 404
        System.delete(review_id, Reviews)
        return jsonify({"Message":"Successfully review deleted."}), 204
    except:
        return jsonify({"Message":"Review not found."}), 404
