#!/bin/bash

# Simple Start Script for Render Deployment
echo "🚀 Starting Flask application with Gunicorn..."

# Set Flask environment
export FLASK_APP=main.py
export FLASK_ENV=production

# Get port from environment variable (Render sets this)
PORT=${PORT:-10000}

# Run the Flask application with Gunicorn
gunicorn --bind 0.0.0.0:$PORT --workers 2 --worker-class sync --timeout 30 --max-requests 1000 --max-requests-jitter 100 main:app 