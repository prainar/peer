# Day 4: profile-edit-backend

## 🎯 Goal

Implement backend functionality for user profile management, including data updates, image handling, and frontend integration.

## 📚 Learning Outcomes

- Create secure profile update endpoints
- Implement image upload and storage
- Set up file validation and processing
- Handle profile data validation
- Implement proper error handling
- Set up secure file serving
- Integrate frontend with backend

## 🚀 Getting Started

Ensure your Day 3 profile UI implementation is complete and working. You should have a good understanding of file handling in Flask, database operations, and basic image processing concepts. The frontend should be ready for backend integration.

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
- Use simple database creation (no complex migrations for beginners)
- Set up model relationships

**⚠️ Note:** For beginners, use `db.create_all()` instead of complex migration tools.


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

### Frontend Integration

#### Implement Profile Data Endpoints

- Create `GET /api/profile` endpoint
- Add `PUT /api/profile` endpoint
- Create `POST /api/profile/image` endpoint
- Handle authentication headers

#### Set up Data Fetching

- Add loading states
- Implement error handling
- Cache profile data
- Handle offline scenarios

### Security Features

#### Basic File Validation

- Check file type (only allow images: jpg, png)
- Set maximum file size (5MB)
- Basic file naming (use timestamp)

#### Basic File Serving

- Set up secure file paths
- Basic access control (only logged-in users)
- Store files in a separate directory

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
- Test frontend-backend integration

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 4: Implement profile edit backend and frontend integration"
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



## ⚠️ Common Problems & Solutions

### Import Errors
- **Problem:** `ModuleNotFoundError: No module named 'app'`
- **Solution:** Use absolute imports, not relative imports
- **Example:** Use `from models.user import User` instead of `from ..models.user import User`

### Directory Issues
- **Problem:** `ImportError: attempted relative import beyond top-level package`
- **Solution:** Always run your app from the project root directory
- **Example:** Run `python main.py` from `/your-project/`, not from `/your-project/models/`

### Database Issues
- **Problem:** Tables not created
- **Solution:** Use `db.create_all()` in your main.py, not complex migrations for beginners

### Virtual Environment Issues
- **Problem:** Package not found
- **Solution:** Always activate your virtual environment first
- **Command:** `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)


## ✅ Deliverable

A secure and robust backend system with:

- Working profile update endpoints
- Secure image upload and processing
- Proper validation and error handling
- Security measures implemented
- Frontend integration complete
- Clean, documented code
- All tests passing

