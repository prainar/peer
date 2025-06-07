# Day 5: Connections

## 🎯 Goal

Build the **Connections** module of the Prok Professional Networking app. This module covers both frontend and backend for managing user connections (friend requests, accept/decline, and viewing connections).

## 📚 Learning Outcomes

- Understand the core concepts of user connections in social platforms.
- Implement a clean and modern UI for managing connections using React and Tailwind CSS.
- Integrate frontend components with a Flask backend API.
- Learn best practices for component separation, API usage, and secure data handling.
- Connect the backend to a database for persistent connection storage.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `day5-connections` folder.
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

   - Build connection request and management components using React and Tailwind CSS.
   - Add UI for sending, accepting, and declining requests.
   - Connect components to backend APIs using fetch/axios.
   - Display error messages and loading states for better UX.

3. **Backend Implementation**

   - Create Flask API endpoints for `/connections` (GET, POST, PUT, DELETE).
   - Use models (e.g., `connection.py`, `user.py`) to interact with the database.
   - Implement authentication and secure connection management.
   - Return appropriate responses and error codes.

4. **Database Integration**

   - Set up a database (e.g., SQLite or PostgreSQL) for connection storage.
   - Ensure connection data is stored securely and can be retrieved/updated.

5. **Testing**
   - Test the full connection flow: send, accept, decline, view, error handling.
   - Ensure the UI updates correctly based on API responses.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for connection cards.
  - Real-time updates for requests.
  - Improved UX flow (e.g., notifications, loading spinners).
- Document your improvement in your own words at the end of this README.

## ✅ Deliverable

A working connections module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd day5-connections
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
day5-connections/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      connection.py
      user.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added real-time notifications for new connection requests using WebSockets. This improves user engagement and responsiveness.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
