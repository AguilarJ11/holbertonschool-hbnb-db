from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from hbnb_final_fase import db, create_app
from hbnb_final_fase.models.users import Users

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])

def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = Users.query.filter_by(email=email).first()

    if user and user.check_password(password):
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=email, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Wrong email or password"}), 401