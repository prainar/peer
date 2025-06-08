# Day 10: Connections

## 🎯 Goal

Build the **Connections** module of the Prok Professional Networking app. This module focuses on displaying and managing your established connections (users you are already connected with).

## 📚 Learning Outcomes

- Understand the concept of a professional network and established connections.
- Implement a clean and modern UI for viewing and managing connections using React and Tailwind CSS.
- Integrate frontend components with a Flask backend API to fetch and manage connections.
- Learn best practices for component separation, API usage, and secure data handling.
- Connect the backend to a database for persistent connection storage.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `10-connections` folder.
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

   - Build a UI to display the list of users you are connected with (your network).
   - Add options to search, filter, or remove connections (optional).
   - Show user details (name, avatar, headline, etc.) for each connection.
   - Do not include pending requests (handled in the previous module).

3. **Backend Implementation**

   - Create Flask API endpoints for `/connections` (GET, DELETE) to fetch and remove established connections.
   - Use models (e.g., `connection.py`, `user.py`) to interact with the database.
   - Implement authentication and secure connection management.
   - Return appropriate responses and error codes.

4. **Testing**
   - Test viewing, searching, and removing connections.
   - Ensure the UI updates correctly based on API responses.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for connection cards.
  - Real-time updates for changes in your network.
  - Improved UX flow (e.g., notifications, loading spinners).
- Document your improvement at the end of this README.

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
   cd 10-connections
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
   - Open your browser and go to `http://localhost:3000/connections` to view your network.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
10-connections/
  README.md
  final/         # Your completed solution goes here
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

> **Bonus Improvement:** Added search and filter options to the connections list for easier navigation.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
