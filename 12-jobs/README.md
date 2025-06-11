# Day 14: Jobs

## 🎯 Goal

Build the **Jobs** module of the Prok Professional Networking app. This module is focused on the details of a specific job and the application process.

## 📚 Learning Outcomes

- Show detailed information for a selected job (full description, requirements, company info, etc.)
- Implement a UI for users to apply to the job (application form, upload resume, etc.)
- (Optional) Show application status or confirmation
- Integrate frontend components with a Flask backend API
- Learn best practices for secure data handling and user workflows

## 📸 Preview

<img src="jobs.png" alt="Jobs" width="120"/>

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `14-jobs` folder.
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

   - Build a UI to show detailed information for a selected job (description, requirements, company info, etc.)
   - Add an application form for users to apply to the job (upload resume, etc.)
   - (Optional) Show application status or confirmation after applying
   - Handle loading, error, and empty states

3. **Backend Integration**

   - Connect to backend endpoints for fetching job details and submitting applications
   - Ensure proper authentication and error handling

4. **Testing**
   - Test viewing job details, applying to jobs, and application status/confirmation
   - Test UI with no jobs, many jobs, and error scenarios

## ✅ Deliverable

A working jobs module with a clean UI and functional backend, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd 14-jobs
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
   - Open your browser and go to `http://localhost:3000/jobs/:jobId` to view job details and apply.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
14-jobs/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      job.py
      application.py
      user.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
