# Day 2: Authentication Backend

## 🎯 Goal

Implement Authentication Backend using Flask and connect it to the frontend UI.

## 📚 Learning Outcomes

- Implement user authentication in Flask
- Set up JWT token-based authentication
- Create secure password hashing
- Implement user registration and login endpoints
- Connect frontend authentication UI with backend
- Handle authentication errors and responses

## 🚀 Getting Started

Ensure your Day 1 setup is complete and all dependencies are installed. You should have separate frontend and backend directories. Basic understanding of JWT and Flask routes/middleware is required.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-2-authentication
```

> **What's happening?** You're creating an independent line of development for this day's tasks.

### Set Up Development Environment

#### Backend Virtual Environment (if not already active from previous day):

```bash
cd backend
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### Install Backend Dependencies:

```bash
pip install Flask-SQLAlchemy Flask-Migrate Werkzeug PyJWT Flask-JWT-Extended Flask-CORS
```

#### Frontend (already set up from Day 1):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Backend Implementation

#### Set up User Model and Database

Configure `app.py` to use SQLAlchemy and define a User model with fields: id, username, email, and password_hash. Integrate password hashing using werkzeug.security's generate_password_hash and check_password_hash.

```bash
flask db init
flask db migrate -m "Initial migration: Create User table"
flask db upgrade
```

#### Create Registration Endpoint (POST /api/signup)

- **Purpose:** Handle new user registration
- **Request Body:** username, email, and password
- **Backend Logic:**
  - Hash the received password
  - Create a new User instance
  - Add the new user to the database
  - Handle existing email/username conflicts
- **Responses:**
  - Success: 201 Created with user data
  - Error: 400 Bad Request for invalid data

#### Create Login Endpoint (POST /api/login)

- **Purpose:** Authenticate users and provide JWT token
- **Request Body:** email/username and password
- **Backend Logic:**
  - Verify credentials
  - Generate JWT token
  - Return token and user data
- **Responses:**
  - Success: 200 OK with token
  - Error: 401 Unauthorized for invalid credentials

### Frontend Integration

#### Connect Login Form to Backend

- Modify the Login component to make POST requests to `/api/login`
- Send credentials from form state
- Handle loading states and errors

#### Handle Authentication Responses

- Parse JSON responses from the backend
- Display success/error messages in the UI
- Use useState for UI message management

#### Implement Token Storage

- Extract token from login response
- Store token securely in localStorage
- Add token to subsequent API requests

### Security Features

- Implement password validation (minimum 8 characters, special characters)
- Add rate limiting for auth endpoints
- Set up CORS for frontend-backend communication
- Add input sanitization for all user inputs

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

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

### Testing

- Test registration flow with valid and invalid data
- Test login flow with correct and incorrect credentials
- Test token validation and expiration
- Test protected route access
- Test error handling and user feedback

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 2: Implement authentication backend and frontend integration"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-2-authentication
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-2-authentication
git push origin main
```

## 📸 Preview

![Authentication Flow](https://i.imgur.com/LQZxGp1.png)
![JWT Token Structure](https://i.imgur.com/MQZxGp2.png)
![API Endpoints](https://i.imgur.com/NQZxGp3.png)

## ✅ Deliverable

A fully functional authentication system with:

- Secure backend implementation with JWT
- Frontend integration with protected routes
- Proper error handling and user feedback
- All tests passing
- Clean, documented code

## 🗂️ Folder Structure

```
02-authentication-backend/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      user.py
    routes/
      auth.py
    middleware/
      auth.py
  frontend/      # React frontend code
    package.json
    src/
      services/
        auth.js
      components/
        Login.jsx
        Signup.jsx
      App.jsx
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
