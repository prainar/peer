# Day 4: Profile Edit Backend

## 🎯 Goal

Implement backend functionality for user profile management, including data updates and image handling.

## 📚 Learning Outcomes

- Create secure profile update endpoints
- Implement image upload and storage
- Set up file validation and processing
- Handle profile data validation
- Implement proper error handling
- Set up secure file serving

## 🚀 Getting Started

Ensure your Day 3 profile UI implementation is complete and working. You should have a good understanding of file handling in Flask, database operations, and basic image processing concepts.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-4-profile-backend
```

> **What's happening?** You're creating an independent line of development for this day's tasks.

### Set Up Development Environment

#### Backend Virtual Environment (if not already active):

```bash
cd backend
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### Install Additional Dependencies:

```bash
pip install Pillow python-magic Flask-Limiter
```

### Profile Data Management

#### Set up Profile Data Model

- Extend User model with profile fields
- Add validation rules for each field
- Implement database migrations
- Set up model relationships

```bash
flask db migrate -m "Add profile fields to User model"
flask db upgrade
```

#### Create Profile Update Endpoint (PUT /api/profile)

- **Purpose:** Handle profile data updates
- **Request Body:** Profile fields to update
- **Backend Logic:**
  - Validate incoming data
  - Update user profile
  - Handle partial updates
  - Return updated profile
- **Responses:**
  - Success: 200 OK with updated profile
  - Error: 400 Bad Request for invalid data

### Image Upload Implementation

#### Set up File Upload Handling

- Configure upload directory
- Set up file size limits
- Implement file type validation
- Create secure file naming

#### Implement Image Processing

- Add image compression
- Handle image resizing
- Generate thumbnails
- Implement format conversion

#### Create Image Upload Endpoint (POST /api/profile/image)

- **Purpose:** Handle profile image uploads
- **Request Body:** Multipart form data with image
- **Backend Logic:**
  - Validate file type and size
  - Process and store image
  - Update user profile
  - Return image URL
- **Responses:**
  - Success: 200 OK with image URL
  - Error: 400 Bad Request for invalid file

### Security Features

#### Implement File Validation

- Add file type whitelist
- Set maximum file size
- Validate image dimensions
- Check file content type

#### Set up Secure File Serving

- Configure secure file paths
- Implement access control
- Add file expiration
- Set up CDN integration

### Run the Application

```bash
# Start the backend server
cd backend
flask run
```

The application will be available at:

- Backend API: http://localhost:5000

### Testing

- Test profile updates with valid and invalid data
- Test image uploads with various file types
- Test file size and type validation
- Test security measures and access control
- Test error handling and recovery
- Test rate limiting and abuse prevention

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 4: Implement profile edit backend"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-4-profile-backend
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-4-profile-backend
git push origin main
```

## 📸 Preview

![Profile API](https://i.imgur.com/RQZxGp7.png)
![Data Flow](https://i.imgur.com/SQZxGp8.png)
![Database Schema](https://i.imgur.com/TQZxGp9.png)

## ✅ Deliverable

A secure and robust backend system with:

- Working profile update endpoints
- Secure image upload and processing
- Proper validation and error handling
- Security measures implemented
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
04-profile-edit-backend/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      profile.py
    routes/
      profile.py
    utils/
      file_handler.py
      image_processor.py
    config/
      upload.py
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
