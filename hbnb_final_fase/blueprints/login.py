from flask import Blueprint, request, jsonify
from hbnb_final_fase.b_logic.system import System
from hbnb_final_fase.models.users import Users

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
     username = request.json.get('username', None)
     password = request.json.get('password', None)
     #user = User.query.filter_by(username=username).first()  # Cambiar implementación, solo es placeholder
     #if user and bcrypt.check_password_hash(user.password, password): # Cambiar implementación, solo es placeholder
        # access_token = create_access_token(identity=username)  # Cambiar implementación, solo es placeholder
        # return jsonify(access_token=access_token), 200  # Cambiar implementación, solo es placeholder
    # return 'Wrong username or password', 401  # Cambiar implementación, solo es placeholder