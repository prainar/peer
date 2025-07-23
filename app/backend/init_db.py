#!/usr/bin/env python3
"""
Database Initialization Script
Creates database tables without importing main.py
"""

import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

def init_database():
    """Initialize the database and create all tables"""
    
    # Create Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    
    # Import models
    from models.user import User
    from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto
    from models.post import Post
    
    # Create all tables
    with app.app_context():
        db.create_all()
        print('✅ Database tables created successfully!')

if __name__ == "__main__":
    init_database() 