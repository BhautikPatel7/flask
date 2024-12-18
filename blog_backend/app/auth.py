from flask import Blueprint, request, jsonify
from . import db, bcrypt
from .models import User
from flask_jwt_extended import create_access_token

auth = Blueprint("auth",__name__)

@auth.route('/register', method =["POST"])
def redister():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email = email).first() :
         return jsonify({'error': 'User already exists'}), 400
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Generate token
    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200