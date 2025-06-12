# Day 11: Job Board

## 🎯 Goal

Implement the Job Board & Application UI (frontend) and corresponding backend API endpoints.

## 📚 Learning Outcomes

- Create job listing interface
- Implement job search functionality
- Design job application system
- Create job filtering system
- Implement job recommendations
- Handle job application process

## 🚀 Getting Started

Ensure your Day 10 Navigation System is complete and tested. You should understand search algorithms and file handling. The backend and frontend should be set up and running.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-11-job-board
```

> **What's happening?** You're creating an independent line of development for this day's tasks.

### Set Up Development Environment

#### Backend Virtual Environment (if not already active):

```bash
cd backend
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### Install Additional Dependencies:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate python-dotenv
```

#### Frontend (already set up from previous days):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Frontend Implementation

#### Create Job Board Components

- Design and implement job listing component
- Create job search functionality
- Add job filtering system
- Implement job details view
- Create application form
- Add job recommendations

### Backend Implementation

#### Set Up Job Management System

- Create job and application models
- Implement job listing endpoints
- Add search functionality
- Create application system
- Implement recommendation engine
- Add job analytics

### Application Process

#### Implement Job Application System

- Create comprehensive application form
- Implement file upload functionality
- Add progress tracking system
- Create status update mechanism
- Implement notification system
- Add application history tracking

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

- Frontend: http://localhost:3000/jobs
- Backend API: http://localhost:5000

### Testing

- Test job search functionality
- Test filtering system
- Test application process
- Test file uploads
- Test notifications
- Test recommendations

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 11: Implement job board and application system"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-11-job-board
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-11-job-board
git push origin main
```

## 📸 Preview

![Job Listings](https://i.imgur.com/4SZxGp1.png)
![Job Details](https://i.imgur.com/5SZxGp2.png)
![Job Search](https://i.imgur.com/6SZxGp3.png)

## ✅ Deliverable

A fully functional job board system with:

- Working job search and filtering
- Complete application process
- File upload functionality
- Notification system
- Recommendation engine
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
11-job-board/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      job.py
      application.py
    routes/
      jobs.py
      applications.py
    services/
      search.py
      recommendations.py
    utils/
      file_handler.py
  frontend/      # React frontend code
    package.json
    src/
      components/
        Jobs/
          JobList.jsx
          JobCard.jsx
          JobSearch.jsx
          JobFilters.jsx
          ApplicationForm.jsx
      hooks/
        useJobs.js
        useApplications.js
      services/
        jobs.js
        applications.js
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
