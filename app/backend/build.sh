#!/bin/bash

# Build script for Render deployment
echo "🚀 Starting build process..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements-render.txt

# Create instance directory
echo "📁 Creating instance directory..."
mkdir -p instance

# Set proper permissions
echo "🔐 Setting proper permissions..."
chmod 755 instance

# Initialize database
echo "🗄️ Initializing database..."
python3 init_db.py

# Create test user
echo "👤 Creating test user..."
python3 create_test_user.py

echo "✅ Build completed successfully!" 