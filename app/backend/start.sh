#!/bin/bash

# Start Script for Render Deployment
echo "🚀 Starting Flask application with Gunicorn..."

# Set Flask environment
export FLASK_APP=main.py
export FLASK_ENV=production

# Run the Flask application with Gunicorn
gunicorn --config gunicorn_config.py main:app 