import os
from datetime import timedelta

class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    
    # Database - Production configuration for Render
    # Use SQLite for now to avoid PostgreSQL compatibility issues
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///instance/app.db')
    
    # Force SQLite for now to avoid psycopg compatibility issues
    if database_url.startswith('postgres://') or database_url.startswith('postgresql://'):
        print("⚠️ PostgreSQL detected, but using SQLite for compatibility")
        database_url = 'sqlite:///instance/app.db'
    
    # Ensure instance directory exists
    import os
    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path, exist_ok=True)
        print(f"✅ Created instance directory: {instance_path}")
    
    # Use absolute path for SQLite database
    if database_url.startswith('sqlite:///'):
        db_path = os.path.join(instance_path, 'app.db')
        database_url = f'sqlite:///{db_path}'
        print(f"🔧 Using absolute database path: {db_path}")
    
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # CORS Configuration - Production only
    CORS_HEADERS = 'Content-Type'
    CORS_ORIGINS = [
        "https://peer-frontend.onrender.com",
        "https://peer-frontend-yfr4.onrender.com",
    ]
    
    # Additional CORS settings
    CORS_SUPPORTS_CREDENTIALS = False
    CORS_ALLOW_HEADERS = ["Content-Type", "Authorization"]
    CORS_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"] 
