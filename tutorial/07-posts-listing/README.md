# Day 7: Posts Listing

## 🎯 Goal

Implement Posts Listing UI (frontend) and integrate with the backend API to fetch existing posts.

## 📚 Learning Outcomes

- Create responsive post listing components
- Implement infinite scrolling
- Handle post data fetching
- Create post filtering system
- Implement post sorting
- Design efficient data loading

## 🚀 Getting Started

Ensure your Day 6 First Deployment is complete and tested. You should understand React hooks and API integration. The backend and frontend should be set up and running.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-7-posts-listing
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
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

#### Frontend (already set up from previous days):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Frontend Implementation

#### Create Post List Component

- Design a responsive list for displaying posts
- Implement infinite scroll using a custom hook
- Add post filtering and sorting options
- Implement loading and error states

### Backend Integration

#### Create Post Listing Endpoints

- Implement GET /api/posts with pagination, filtering, and sorting
- Optimize queries for performance
- Add data caching for frequently accessed posts

### Performance Optimization

- Implement lazy loading for images and data
- Add request debouncing for filters and search
- Use virtual scrolling for large lists
- Optimize API calls and reduce re-renders

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

- Frontend: http://localhost:3000/posts
- Backend API: http://localhost:5000

### Testing

- Test infinite scroll with large data sets
- Test filtering and sorting functionality
- Test loading and error states
- Test performance and responsiveness

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 7: Implement posts listing UI and backend integration"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-7-posts-listing
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-7-posts-listing
git push origin main
```

## 📸 Preview

<img src="posts-listing.png" alt="Posts Listing UI" width="120"/>

## Preview

![Posts Feed](https://i.imgur.com/1RZxGp7.png)
![Post Card](https://i.imgur.com/2RZxGp8.png)
![Infinite Scroll](https://i.imgur.com/3RZxGp9.png)

## Overview

## ✅ Deliverable

A performant and responsive post listing system with:

- Infinite scrolling
- Filtering and sorting
- Efficient data loading
- Proper error handling
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
07-posts-listing/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    routes/
      posts.py
    services/
      post_service.py
    utils/
      pagination.py
  frontend/      # React frontend code
    package.json
    src/
      components/
        Posts/
          PostList.jsx
          PostCard.jsx
          PostFilter.jsx
          InfiniteScroll.jsx
      hooks/
        useInfiniteScroll.js
        usePosts.js
      services/
        posts.js
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
