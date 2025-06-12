# Day 5: Post Creation

## 🎯 Goal

Build Post Creation UI (frontend) and implement the necessary backend logic for storing posts.

## 📚 Learning Outcomes

- Create post creation interface
- Implement rich text editing
- Handle media uploads
- Create post storage system
- Implement post validation
- Design user-friendly post creation flow

## 🚀 Getting Started

Ensure your Day 4 Profile Backend is complete and working. You should understand rich text editing and media handling. The backend and frontend should be set up and running.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-5-post-creation
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
pip install Flask Flask-SQLAlchemy Flask-Migrate Pillow python-magic
```

#### Frontend (already set up from previous days):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Frontend Implementation

#### Create Post Creation Form

- Design a form for post content, media, and preview
- Implement a rich text editor for post body
- Add media upload (image/video) functionality
- Create a post preview component
- Implement form validation and loading states

### Backend Implementation

#### Create Post Model and Endpoints

- Define a Post model with fields: id, user_id, content, media_url, created_at, etc.
- Implement POST /api/posts endpoint for creating posts
- Set up media storage and validation
- Add post metadata and indexing

### Media Handling

#### Implement Image and Video Upload

- Set up file upload handling for images and videos
- Validate file type and size
- Process and store media files
- Generate media URLs for frontend display

### Run the Application

```bash
# Start the backend server (in one terminal)
cd backend
flask run

# Start the frontend development server (in another terminal)
cd frontend
npm run dev
```

The application will be available at:

- Frontend: http://localhost:3000/create-post
- Backend API: http://localhost:5000

### Testing

- Test post creation with and without media
- Test media uploads (image and video)
- Test form validation and error handling
- Test loading states and user feedback

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 5: Implement post creation UI and backend logic"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-5-post-creation
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-5-post-creation
git push origin main
```

## 📸 Preview

<img src="post-creation.png" alt="Post Creation UI" width="120"/>

## Preview

![Post Creation Form](https://i.imgur.com/UQZxGp1.png)
![Rich Text Editor](https://i.imgur.com/VQZxGp2.png)
![Media Upload](https://i.imgur.com/WQZxGp3.png)

## Overview

## ✅ Deliverable

A fully functional post creation system with:

- Rich text editing
- Media upload and preview
- Proper validation and error handling
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
05-post-creation/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      post.py
    routes/
      posts.py
    services/
      media_processing.py
    utils/
      validation.py
  frontend/      # React frontend code
    package.json
    src/
      components/
        Post/
          PostCreation.jsx
          RichTextEditor.jsx
          MediaUpload.jsx
          PostPreview.jsx
      services/
        posts.js
        media.js
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
