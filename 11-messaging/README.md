# Day 6: Messaging

## 🎯 Goal

Build the **Messaging** module of the Prok Professional Networking app. This module covers both frontend and backend for real-time or asynchronous user messaging.

## 📚 Learning Outcomes

- Understand the core concepts of messaging systems in web applications.
- Implement a clean and modern UI for chat and message threads using React and Tailwind CSS.
- Integrate frontend components with a Flask backend API.
- Learn best practices for component separation, API usage, and secure message handling.
- Connect the backend to a database for persistent message storage.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `day6-messaging` folder.
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

   - Build chat UI and message thread components using React and Tailwind CSS.
   - Add form validation for message input.
   - Connect components to backend APIs using fetch/axios or WebSockets.
   - Display error messages and loading states for better UX.

3. **Backend Implementation**

   - Create Flask API endpoints for `/messages` (GET, POST).
   - Use models (e.g., `message.py`, `user.py`) to interact with the database.
   - Implement authentication and secure message storage.
   - Return appropriate responses and error codes.

4. **Database Integration**

   - Set up a database (e.g., SQLite or PostgreSQL) for message storage.
   - Ensure message data is stored securely and can be retrieved efficiently.

5. **Testing**
   - Test the full messaging flow: send, receive, error handling.
   - Ensure the UI updates correctly based on API responses.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for chat bubbles.
  - Real-time updates using WebSockets.
  - Improved UX flow (e.g., typing indicators, loading spinners).
- Document your improvement in your own words at the end of this README.

## ✅ Deliverable

A working messaging module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd day6-messaging
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
day6-messaging/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      message.py
      user.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added real-time chat using Flask-SocketIO and React context. This allows users to see new messages instantly.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
