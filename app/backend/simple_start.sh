#!/bin/bash

# Simple Start Script for Render Deployment
echo "🚀 Starting Flask application with Gunicorn..."

# Set Flask environment
export FLASK_APP=main.py
export FLASK_ENV=production

# Create instance directory with proper permissions
echo "📁 Creating instance directory..."
mkdir -p instance
chmod 755 instance

# Create upload directories with proper permissions
echo "📁 Creating upload directories..."
mkdir -p uploads/post_photos
chmod 755 uploads
chmod 755 uploads/post_photos

# Initialize database and create test user (with timeout)
echo "🗄️ Initializing database..."
timeout 30s python3 init_db.py || echo "⚠️ Database initialization failed or timed out, continuing..."

echo "👤 Creating test user..."
timeout 30s python3 create_test_user.py || echo "⚠️ Test user creation failed or timed out, continuing..."

# Get port from environment variable (Render sets this)
PORT=${PORT:-10000}

# Run the Flask application with Gunicorn
echo "🌐 Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:$PORT --workers 1 --worker-class sync --timeout 60 --max-requests 1000 --max-requests-jitter 100 main:app 