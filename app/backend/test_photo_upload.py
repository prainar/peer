#!/usr/bin/env python3
"""
Test script for photo upload functionality
"""

import os
import tempfile
from io import BytesIO
from PIL import Image
import requests
import json

def create_test_image():
    """Create a simple test image"""
    # Create a simple 100x100 test image
    img = Image.new('RGB', (100, 100), color='red')
    
    # Save to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    
    return img_bytes

def test_profile_photo_upload():
    """Test profile photo upload"""
    print("🧪 Testing profile photo upload...")
    
    # Create test image
    img_bytes = create_test_image()
    
    # Test data
    test_data = {
        'photo_url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k='
    }
    
    # Test with base64 data URL
    try:
        response = requests.post(
            'http://localhost:5000/api/profile/photo',
            headers={'Content-Type': 'application/json'},
            json=test_data
        )
        print(f"✅ Base64 upload test: {response.status_code}")
        if response.status_code == 201:
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Base64 upload test failed: {e}")
    
    # Test with file upload
    try:
        files = {'photo': ('test.jpg', img_bytes, 'image/jpeg')}
        response = requests.post(
            'http://localhost:5000/api/profile/photo',
            files=files
        )
        print(f"✅ File upload test: {response.status_code}")
        if response.status_code == 201:
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ File upload test failed: {e}")

def test_post_photo_upload():
    """Test post photo upload"""
    print("\n🧪 Testing post photo upload...")
    
    # Create test image
    img_bytes = create_test_image()
    
    try:
        files = {'photo': ('test.jpg', img_bytes, 'image/jpeg')}
        response = requests.post(
            'http://localhost:5000/api/posts/photo',
            files=files
        )
        print(f"✅ Post photo upload test: {response.status_code}")
        if response.status_code == 201:
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Post photo upload test failed: {e}")

if __name__ == "__main__":
    print("🚀 Starting photo upload tests...")
    test_profile_photo_upload()
    test_post_photo_upload()
    print("\n✅ Photo upload tests completed!") 