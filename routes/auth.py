from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.models import User
from app import db
from utils.email_service import send_verification_email
from utils.encryption import encrypt_link

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, role='Client')
    db.session.add(new_user)
    db.session.commit()

    send_verification_email(data['email'], new_user.id)

    return jsonify({'message': 'User created successfully, verification email sent!'}), 201

@auth_bp.route('/verify-email', methods=['GET'])
def verify_email():
    token = request.args.get('token')
    user_id = request.args.get('id')
    email = decrypt_link(token)

    user = User.query.get(user_id)
    if user and user.email == email:
        return jsonify({'message': 'Email verified successfully!'}), 200
    return jsonify({'message': 'Invalid verification link!'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'access_token': access_token}), 200
