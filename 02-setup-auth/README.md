# Day 1: Setup Auth

## 🎯 Goal

Build the **Setup Auth** module of the Prok Professional Networking app. This module covers both frontend and backend authentication, including user registration and login.

## 📚 Learning Outcomes

- Understand the core concepts of authentication in web applications.
- Implement a clean and modern UI for login and signup using React and Tailwind CSS.
- Integrate frontend components with a Flask backend API.
- Learn best practices for component separation, API usage, and secure authentication.
- Connect the backend to a database for persistent user storage.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `day1-setup-auth` folder.
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

   - Build login and signup forms using React and Tailwind CSS.
   - Add form validation for user input (email, password, etc.).
   - Connect forms to backend APIs using fetch/axios.
   - Display error messages and loading states for better UX.

3. **Backend Implementation**

   - Create Flask API endpoints for `/register` and `/login`.
   - Use models (e.g., `user.py`) to interact with the database.
   - Implement password hashing and secure authentication.
   - Return appropriate responses and error codes.

4. **Database Integration**

   - Set up a database (e.g., SQLite or PostgreSQL) for user storage.
   - Ensure user data is stored securely and can be retrieved for login.

5. **Testing**
   - Test the full authentication flow: registration, login, error handling.
   - Ensure the UI updates correctly based on API responses.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for forms and buttons.
  - Additional validation (e.g., password strength meter).
  - Improved UX flow (e.g., redirect after login, loading spinners).
- Document your improvement in your own words at the end of this README.

## ✅ Deliverable

A working authentication module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd day1-setup-auth
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
   - Open your browser and go to `http://localhost:3000` for the frontend.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
day1-setup-auth/
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

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added a password strength meter to the signup form using a custom React component. This helps users create stronger passwords and improves security.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
