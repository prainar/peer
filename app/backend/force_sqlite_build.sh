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
import sqlite3
import os

# Create instance directory if it doesn't exist
os.makedirs('instance', exist_ok=True)

# Create a simple database with basic tables
conn = sqlite3.connect('instance/app.db')
cursor = conn.cursor()

# Create user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Create profile table
cursor.execute('''
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    full_name VARCHAR(120),
    bio TEXT,
    location VARCHAR(120)
)
''')

# Create skill table
cursor.execute('''
CREATE TABLE IF NOT EXISTS skill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    name VARCHAR(80) NOT NULL,
    FOREIGN KEY (profile_id) REFERENCES profile (id)
)
''')

# Create experience table
cursor.execute('''
CREATE TABLE IF NOT EXISTS experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    title VARCHAR(120) NOT NULL,
    company VARCHAR(120) NOT NULL,
    start_date VARCHAR(50),
    end_date VARCHAR(50),
    description TEXT,
    FOREIGN KEY (profile_id) REFERENCES profile (id)
)
''')

# Create education table
cursor.execute('''
CREATE TABLE IF NOT EXISTS education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    school VARCHAR(120) NOT NULL,
    degree VARCHAR(120),
    field_of_study VARCHAR(120),
    start_year INTEGER,
    end_year INTEGER,
    FOREIGN KEY (profile_id) REFERENCES profile (id)
)
''')

# Create achievement table
cursor.execute('''
CREATE TABLE IF NOT EXISTS achievement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    title VARCHAR(120) NOT NULL,
    description TEXT,
    date VARCHAR(50),
    image_url VARCHAR(255),
    FOREIGN KEY (profile_id) REFERENCES profile (id)
)
''')

# Create post table
cursor.execute('''
CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    image_url VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user (id)
)
''')

# Create post_like table
cursor.execute('''
CREATE TABLE IF NOT EXISTS post_like (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (post_id) REFERENCES post (id)
)
''')

conn.commit()
conn.close()
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