#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
country_bp = Blueprint('country', __name__)


@country_bp.route('/countries', methods=['GET'])
def get_countries():
    try:
        countries = System.get_all_countries()
        return jsonify({"Message":"Successfully retrieved all Countries.", "Countries":countries}), 200
    except:
        return jsonify({"Message":"Countries not found."}), 404

@country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    if not country_code:
        raise ValueError("Code not valid!")
    try:
        country = System.get_country(country_code)
        return jsonify({"Message":"Successfully retrieved Country", "Place":country}), 200
    except:
        return jsonify({"Message":"Country not found."}), 404

@country_bp.route('/countries/<ountry_code>/cities', methods=['GET'])
def get_country_cities(country_code):
    try:
        cities = System.get_all('City')
        city_list = []
        for city in cities:
            if city.get("country_code") == country_code:
                city_list.append(city)
        if not city_list:
            raise ValueError(f"There are no citys from {country_code} country")
        return jsonify({"Message":"Successfully retrieved all citys","Contry":country_code, "Citys":city_list}), 200
    except:
        return jsonify({"Message":"Citys not found."}), 404

@country_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    if not data.get("name"):
        raise ValueError("Name not valid!")
    if not data.get("country_code"):
        raise ValueError("Contry code not valid!")
    try:
        city = System.create_city(data)
        return jsonify(city), 201
    except Exception:
        return jsonify({"Message":"Failed to create City."}), 400

@country_bp.route('/cities', methods=['GET'])
def get_cities():
    try:
        cities = System.get_all('City')
        return jsonify(cities), 200
    except:
        return jsonify({"Message":"Citys not found."}), 404

@country_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    if not city_id:
        raise ValueError("Id not valid!")
    try:
        city = System.get(city_id, 'City')
        return jsonify(city), 200
    except:
        return jsonify({"Message":"City not found."}), 404

@country_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    if not data.get("name"):
        raise ValueError("Name not valid!")
    if not data.get("country_code"):
        raise ValueError("Contry code not valid!")
    if not city_id:
        raise ValueError("Id not valid!")
    try:
        city = System.update(city_id, data, 'City')
        return jsonify(city), 200
    except:
        return jsonify({"Message": "City not found"}), 404

@country_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    if not city_id:
        raise ValueError("Id not valid!")
    try:
        city = System.get(city_id, 'City')
        if city == None:
            return jsonify({"Message":"City not found."}), 404
        System.delete(city_id, 'Users')
        return jsonify({"Message":"Successfully City deleted."}), 204
    except:
        return jsonify({"Message":"City not found."}), 404
