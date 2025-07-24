import os
from datetime import timedelta

class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    
    # Database - Production configuration for Render
    # Always use environment variable for production deployment
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/app.db')
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
