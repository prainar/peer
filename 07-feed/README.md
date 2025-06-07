# Day 4: Feed

## 🎯 Goal

Build the **Feed** module of the Prok Professional Networking app. This module covers both frontend and backend for displaying a user's feed with posts and updates.

## 📚 Learning Outcomes

- Understand the core concepts of feed aggregation and display in web applications.
- Implement a clean and modern UI for the feed using React and Tailwind CSS.
- Integrate frontend components with a Flask backend API.
- Learn best practices for component separation, API usage, and efficient data fetching.
- Connect the backend to a database for persistent feed storage.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `day4-feed` folder.
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

   - Build feed components using React and Tailwind CSS.
   - Add loading states and error handling for data fetching.
   - Connect components to backend APIs using fetch/axios.
   - Display posts and updates in a user-friendly format.

3. **Backend Implementation**

   - Create Flask API endpoints for `/feed` (GET).
   - Use models (e.g., `feed.py`, `post.py`) to interact with the database.
   - Implement authentication and efficient feed aggregation.
   - Return appropriate responses and error codes.

4. **Database Integration**

   - Set up a database (e.g., SQLite or PostgreSQL) for feed and post storage.
   - Ensure feed data is stored securely and can be retrieved efficiently.

5. **Testing**
   - Test the full feed flow: display, refresh, error handling.
   - Ensure the UI updates correctly based on API responses.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for feed items.
  - Infinite scroll or pagination.
  - Improved UX flow (e.g., real-time updates, loading spinners).
- Document your improvement in your own words at the end of this README.

## ✅ Deliverable

A working feed module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd day4-feed
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
day4-feed/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      feed.py
      post.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added infinite scroll to the feed using Intersection Observer in React. This allows users to seamlessly browse more content.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
