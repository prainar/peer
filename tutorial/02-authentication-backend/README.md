# Day 2: authentication-backend

## 🎯 Goal

Implement the authentication backend using Flask, and integrate it with the frontend UI.

## 📚 Learning Outcomes

- Implement user authentication in Flask  
- Set up JWT token-based authentication  
- Create secure password hashing  
- Implement user registration and login endpoints  
- Connect frontend authentication UI with backend  
- Handle authentication errors and responses  

## 🚀 Getting Started

Ensure your Day 1 setup is complete and all dependencies are installed. You should have separate `frontend/` and `backend/` directories. Basic understanding of JWT and Flask routes/middleware is required.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Never work directly on the main branch! Always create a new branch for each assignment or distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main

# Now, create and switch to a new branch for this assignment
git checkout -b day-2-authentication
```

> **What's happening?** You're creating an isolated branch to implement your authentication logic without modifying the main branch prematurely.

### Set Up Development Environment

#### Backend Environment (Reactivate if needed)

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Backend Dependencies

```bash
pip install Flask-SQLAlchemy Flask-Migrate Werkzeug PyJWT Flask-JWT-Extended Flask-CORS
```

> These libraries will help manage your database, secure passwords, and enable token-based authentication with cross-origin support.

#### Frontend Preparation

Ensure your frontend already has dependencies installed from Day 1:

```bash
cd frontend
npm install
```

### Backend Implementation

#### Database Setup and User Model

- Create a `User` model with fields: `id`, `username`, `email`, and `password_hash`.
- Use `generate_password_hash` and `check_password_hash` from `werkzeug.security`.

```bash
flask db init
flask db migrate -m "Initial migration: Create User table"
flask db upgrade
```

#### Registration Endpoint (POST `/api/signup`)

- **Purpose:** Allow new users to register
- **Input:** `username`, `email`, `password`
- **Logic:**
  - Hash password
  - Save new user
  - Validate uniqueness
- **Responses:**
  - `201 Created` – user created
  - `400 Bad Request` – invalid input or duplicate user

#### Login Endpoint (POST `/api/login`)

- **Purpose:** Authenticate users and issue JWT token
- **Input:** `username/email`, `password`
- **Logic:**
  - Verify credentials
  - Generate JWT token
  - Return token + user data
- **Responses:**
  - `200 OK` – success with token
  - `401 Unauthorized` – incorrect credentials

### Frontend Integration

#### Connect Login Form to Backend

- Send POST request to `/api/login` with form data
- Use `fetch` or `axios` to make request
- Display loading or error states

#### Handle Authentication Responses

- Show success or error messages based on backend response
- Use `useState` to manage feedback and message UI

#### Token Storage and Usage

- Store JWT token in `localStorage`
- Attach token to protected API requests

```js
localStorage.setItem("token", token)
```

### Security Features

- Enforce minimum password complexity
- Add basic rate limiting on auth endpoints
- Set up CORS between frontend and backend
- Sanitize all user inputs

### Run the Application

```bash
# Backend
cd backend
flask run

# Frontend
cd frontend
npm run dev
```

Application available at:

- Frontend: [http://localhost:3000](http://localhost:3000)  
- Backend API: [http://localhost:5000](http://localhost:5000)

### Testing

- Test registration with new and duplicate data
- Test login with valid/invalid credentials
- Confirm JWT token is returned and stored
- Access protected routes with/without token
- Verify frontend error messages display properly

---

### Git Workflow

1. **Develop and Save Your Progress**

```bash
git status
git add .
git commit -m "Day 2: Implement authentication backend and frontend integration"
```

> Use clear commit messages that explain the key changes you've made.

2. **Push Your Changes to Your Fork**

```bash
git push -u origin day-2-authentication
```

> Uploads your branch to your forked repo.

3. **Merge After Assignment Completion**

```bash
git checkout main
git pull origin main
git merge day-2-authentication
git push origin main
```

> Merge your work only once it's been tested and finalized.

---

## 📸 Preview

![Authentication Flow](https://i.imgur.com/LQZxGp1.png)  
![JWT Token Structure](https://i.imgur.com/MQZxGp2.png)  
![API Endpoints](https://i.imgur.com/NQZxGp3.png)

## ✅ Deliverable

A fully functional authentication system:

- Secure user auth with JWT in Flask backend  
- Integrated frontend login with proper token handling  
- Error messaging and form feedback  
- All tests passing and code documented

