#!/bin/bash

# Force SQLite Build Script for Render Deployment
# This script ensures the backend can be deployed on Render with SQLite

echo "🚀 Starting backend build for Render deployment..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements-render.txt

# Create instance directory if it doesn't exist
echo "📁 Creating instance directory..."
mkdir -p instance

# Initialize database (this will create the SQLite file if it doesn't exist)
echo "🗄️ Initializing database..."
python3 -c "
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

from main import app, db

with app.app_context():
    db.create_all()
    print('✅ Database tables created successfully!')
"

# Restore user data
echo "📊 Restoring user data..."
python3 restore_data.py

# Set proper permissions
echo "🔐 Setting proper permissions..."
chmod -R 755 instance/
chmod -R 755 uploads/

echo "✅ Backend build completed successfully!"
echo "🎯 Ready for deployment on Render!" 