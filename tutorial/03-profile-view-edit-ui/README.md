# Day 3: User Profile View & Edit UI

## 🎯 Goal

Develop User Profile View & Edit UI (frontend) and integrate with backend for data retrieval.

## 📚 Learning Outcomes

- Create responsive profile view components
- Implement profile edit functionality
- Design user-friendly forms
- Handle image uploads
- Implement real-time form validation
- Create reusable UI components

## 🚀 Getting Started

Ensure your Day 2 authentication is complete and working. You should have a good understanding of React forms and image handling. The backend should be running and accessible.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-3-profile-ui
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
# Backend
pip install Pillow python-magic

# Frontend
cd ../frontend
npm install react-dropzone axios
```

### Profile View Implementation

#### Create Profile Header Component

- Design a responsive header with user avatar
- Display user's name, title, and location
- Add social media links section
- Implement responsive layout for mobile and desktop

#### Display User Information

- Show user's bio and skills
- Display work experience and education
- Add contact information section
- Implement collapsible sections for mobile

#### Show User Activity

- Display recent posts and interactions
- Show connection count and mutual connections
- Add activity timeline
- Implement lazy loading for activity feed

### Profile Edit Implementation

#### Create Edit Form Components

- Design form layout with sections
- Implement input fields for all profile data
- Add validation rules for each field
- Create reusable form components

#### Implement Form Validation

- Add real-time validation feedback
- Implement custom validation rules
- Show validation error messages
- Handle form submission states

#### Add Image Upload Functionality

- Implement drag-and-drop image upload
- Add image preview functionality
- Handle image compression
- Implement upload progress indicator

### Backend Integration

#### Connect to Profile Data Endpoints

- Implement GET /api/profile endpoint
- Add PUT /api/profile endpoint
- Create POST /api/profile/image endpoint
- Handle authentication headers

#### Implement Data Fetching

- Add loading states
- Implement error handling
- Cache profile data
- Handle offline scenarios

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

- Frontend: http://localhost:3000/profile
- Backend API: http://localhost:5000

### Testing

- Test responsive design on multiple devices
- Test form validation with various inputs
- Test image upload with different file types
- Test error handling and recovery
- Test loading states and transitions
- Test offline functionality

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 3: Implement profile view and edit UI"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-3-profile-ui
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-3-profile-ui
git push origin main
```

## 📸 Preview

![Profile View](https://i.imgur.com/OQZxGp4.png)
![Profile Edit](https://i.imgur.com/PQZxGp5.png)
![Profile Settings](https://i.imgur.com/QQZxGp6.png)

## ✅ Deliverable

A fully functional profile system with:

- Responsive profile view and edit interface
- Working image upload functionality
- Real-time form validation
- Proper error handling and loading states
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
03-profile-view-edit-ui/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    routes/
      profile.py
  frontend/      # React frontend code
    package.json
    src/
      components/
        Profile/
          ProfileHeader.jsx
          ProfileEdit.jsx
          ProfileView.jsx
          ImageUpload.jsx
      services/
        profile.js
      App.jsx
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
