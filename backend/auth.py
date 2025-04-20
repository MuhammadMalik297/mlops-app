from flask import Blueprint, request, jsonify
from utils import hash_password, check_password, generate_token
from models import find_user_by_email, create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if find_user_by_email(data['email']):
        return jsonify({'message': 'User already exists'}), 400
    hashed_pw = hash_password(data['password'])
    create_user(data['email'], hashed_pw)
    return jsonify({'message': 'User created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = find_user_by_email(data['email'])
    if not user or not check_password(data['password'], user['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    token = generate_token(str(user['_id']))
    return jsonify({'token': token}), 200
