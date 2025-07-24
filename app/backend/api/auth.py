from flask import Blueprint, request, jsonify, current_app
from models.user import User, db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
import traceback

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    try:
        print("🔵 Signup request received")
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        print(f"🔵 Signup data: username={username}, email={email}, password_length={len(password) if password else 0}")

        # Password complexity check
        if not password or len(password) < 8:
            print("🔴 Password too short")
            return jsonify({"message": "Password must be at least 8 characters"}), 400

        # Check for existing user
        print("🔵 Checking for existing user...")
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            print("🔴 User already exists")
            return jsonify({"message": "User already exists"}), 400

        print("🔵 Creating new user...")
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print("✅ User created successfully")
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        print(f"🔴 Signup error: {e}")
        print(f"🔴 Traceback: {traceback.format_exc()}")
        return jsonify({"message": "Internal server error during signup"}), 500

@auth_bp.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = None
        if username:
            user = User.query.filter_by(username=username).first()
        elif email:
            user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            token = create_access_token(identity=str(user.id))
            return jsonify({"token": token, "user": {"id": user.id, "username": user.username, "email": user.email}}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"message": "Internal server error during login"}), 500 