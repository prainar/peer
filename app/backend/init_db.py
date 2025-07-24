#!/usr/bin/env python3
"""
Database initialization script for Peer backend
"""

import os
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

def init_database():
    """Initialize the database and create tables using SQLAlchemy"""
    
    # Create Flask app for database initialization
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy
    db = SQLAlchemy(app)
    
    # Import models to register them
    from models.user import User
    from models.post import Post
    from models.job import Job
    from models.message import Message
    from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto
    
    print("🗄️ Initializing database using SQLAlchemy...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully!")
    
        # Check database connection
        try:
            # Test database connection
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
            print("✅ Database connection successful!")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
        
        return True

if __name__ == "__main__":
    success = init_database()
    if success:
        print("✅ Database initialization completed successfully!")
    else:
        print("❌ Database initialization failed!")
        exit(1) 