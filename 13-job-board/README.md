# Day 13 : Job Board

## 🎯 Goal

Build the **Job Board** module of the Prok Professional Networking app. This module is focused on displaying a list of available jobs to users, similar to a job board you’d see on LinkedIn or Indeed.

## 📚 Learning Outcomes

- List all job postings (title, company, location, summary, etc.)
- Allow users to browse and search/filter jobs
- Implement a clean and modern UI for job board listings using React and Tailwind CSS
- Integrate frontend components with a backend API to fetch job data
- Handle loading, error, and empty states gracefully

## 📸 Preview

<!-- Add a screenshot of the job board/listing interface here when available -->

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `13-job-board` folder.
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

   - Build a UI to display a list of job postings (title, company, location, summary, etc.)
   - Add search and filter options for jobs (optional)
   - Do not include job application or job detail views in this module
   - Handle loading, error, and empty states

3. **Backend Integration**

   - Connect to backend endpoints to fetch job listings
   - Ensure proper error handling and data validation

4. **Testing**
   - Test the job board with multiple jobs, no jobs, and error scenarios
   - Ensure the UI updates correctly based on API responses

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Enhanced styling for job cards
  - Pagination or infinite scroll for job listings
  - Improved UX flow (e.g., loading spinners, skeleton loaders)
- Document your improvement at the end of this README

## ✅ Deliverable

A working job board module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd 13-job-board
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
   - Open your browser and go to `http://localhost:3000/job-board` to view the job board.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
13-job-board/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      job.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added pagination to the job board for easier browsing of large job lists.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
