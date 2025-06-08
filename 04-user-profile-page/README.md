# Day 4: User Profile Page

## 🎯 Goal

Build the **User Profile Page** module for the Prok Professional Networking app. This module focuses on displaying another user's public profile in a clean, professional, and read-only format, similar to how you view someone else's profile on real networking platforms.

## 📚 Learning Outcomes

- Understand the difference between self-profile editing and viewing others' profiles.
- Implement a user-friendly, read-only UI for displaying another user's profile using React and Tailwind CSS.
- Fetch and render user data from the backend securely.
- Learn best practices for protecting private data and presenting only public information.
- Handle loading, error, and empty states gracefully in the UI.

## 📸 Preview

![User Profile Page](./user-profile-page.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `04-user-profile-page` folder.
   - Install frontend dependencies in the `frontend` directory:
     ```bash
     cd frontend
     npm install
     ```
   - Install backend dependencies in the `backend` directory:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

2. **Frontend Implementation**

   - Build a read-only user profile page using React and Tailwind CSS.
   - Display public fields: name, headline, bio, experience, education, skills, and profile picture (if available).
   - Fetch another user's data from the backend using their user ID (e.g., via URL parameter).
   - Show loading spinners while fetching data and error messages if the user is not found.
   - Ensure no edit buttons or forms are present for non-owners.

3. **Backend Implementation**

   - Create a Flask API endpoint for `/users/<user_id>` (GET) to return public profile data.
   - Ensure only public fields are returned (no sensitive/private info).
   - Handle cases where the user does not exist (return 404).

4. **Security & Privacy**

   - Do not expose private fields (e.g., email, phone, admin status) in the API response.
   - Validate user permissions if you add any special features (e.g., admin view).

5. **Testing**
   - Test viewing several different users' profiles (including non-existent users).
   - Check that the UI updates correctly for loading, error, and empty states.

## ✅ Deliverable

A working user profile page module that displays another user's public profile in a read-only format, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd 04-user-profile-page
   ```
2. **Install dependencies**
   - Frontend:
     ```bash
     cd frontend
     npm install
     ```
   - Backend:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
3. **Run the applications**
   - Start the backend server:
     ```bash
     cd backend
     flask run
     ```
   - Start the frontend development server:
     ```bash
     cd frontend
     npm start
     ```
4. **Access the app**
   - Open your browser and go to `http://localhost:3000/user/<user_id>` to view a user's profile.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
04-user-profile-page/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      user.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
