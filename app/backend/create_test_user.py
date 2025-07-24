#!/usr/bin/env python3
"""
Create a test user for development and testing
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import Config

def create_test_user():
    """Create a test user in the database"""
    
    # Create Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy
    db = SQLAlchemy(app)
    
    # Import User model
    from models.user import User
    
    with app.app_context():
        # Check if test user already exists
        existing_user = User.query.filter_by(email='test@example.com').first()
        if existing_user:
            print("✅ Test user already exists!")
            print(f"Username: {existing_user.username}")
            print(f"Email: {existing_user.email}")
            return
        
        # Create test user
        test_user = User(
            username='testuser',
            email='test@example.com'
        )
        test_user.set_password('testpassword123')
        
        # Add to database
        db.session.add(test_user)
        db.session.commit()
        
        print("✅ Test user created successfully!")
        print("Username: testuser")
        print("Email: test@example.com")
        print("Password: testpassword123")
        print("\nYou can now use these credentials to login!")

if __name__ == "__main__":
    create_test_user() 