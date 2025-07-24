#!/usr/bin/env python3
"""
Database fix script to ensure ProfilePhoto table exists
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

def fix_database():
    """Fix database by ensuring ProfilePhoto table exists"""
    
    # Create Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy
    db = SQLAlchemy(app)
    
    # Import all models
    from models.user import User
    from models.post import Post, PostLike
    from models.job import Job
    from models.message import Message
    from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto
    
    print("🔧 Fixing database tables...")
    
    with app.app_context():
        # Check current tables
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"🔧 Current tables: {tables}")
        
        # Check if profile_photo table exists
        if 'profile_photo' not in tables:
            print("🔧 ProfilePhoto table missing, creating it...")
            
            # Create the ProfilePhoto table specifically
            ProfilePhoto.__table__.create(db.engine, checkfirst=True)
            print("✅ ProfilePhoto table created!")
        else:
            print("✅ ProfilePhoto table already exists!")
        
        # Verify all critical tables
        critical_tables = ['user', 'profile', 'profile_photo', 'post', 'post_like', 'job', 'message']
        missing_tables = [table for table in critical_tables if table not in tables]
        
        if missing_tables:
            print(f"🔧 Creating missing tables: {missing_tables}")
            db.create_all()
            print("✅ All missing tables created!")
        else:
            print("✅ All critical tables exist!")
        
        # Final verification
        inspector = db.inspect(db.engine)
        final_tables = inspector.get_table_names()
        print(f"🔧 Final tables: {final_tables}")
        
        return True

if __name__ == "__main__":
    success = fix_database()
    if success:
        print("✅ Database fix completed successfully!")
    else:
        print("❌ Database fix failed!")
        exit(1) 