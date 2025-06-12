# Day 12: Second Deployment

## 🎯 Goal

Deploy Milestone 2 of the application, including frontend to Netlify/AWS and backend to Python Anywhere.

## 📚 Learning Outcomes

- Deploy updated React application
- Update Flask backend deployment
- Configure production environment
- Implement monitoring
- Set up analytics
- Configure backup systems

## 🚀 Getting Started

Ensure your Day 11 Job Board is complete and tested. You should have access to deployment platforms and understand production deployment concepts. The application should be ready for deployment.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-12-second-deployment
```

> **What's happening?** You're creating an independent line of development for this day's tasks.

### Set Up Development Environment

#### Prepare Frontend for Deployment:

```bash
cd frontend
npm run build
```

#### Prepare Backend for Deployment:

```bash
cd backend
pip freeze > requirements.txt
```

### Frontend Deployment

#### Deploy to Production

- Update production build configuration
- Configure new features for production
- Set up monitoring and analytics
- Update environment variables
- Configure CDN and caching

### Backend Deployment

#### Deploy to Python Anywhere

- Update Python Anywhere configuration
- Configure new endpoints
- Set up monitoring and logging
- Update database schema
- Configure backup systems

### Production Optimization

#### Optimize Application Performance

- Optimize static assets
- Configure caching strategies
- Set up CDN distribution
- Implement rate limiting
- Configure security measures
- Set up monitoring systems

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

- Test production build
- Test new features in production
- Test monitoring systems
- Test analytics integration
- Test backup systems
- Test security measures

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 12: Implement second deployment with monitoring and analytics"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-12-second-deployment
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-12-second-deployment
git push origin main
```

## 📸 Preview

<img src="second-deployment.png" alt="Second Deployment Process" width="120"/>

## Preview

![Deployment Dashboard](https://i.imgur.com/7SZxGp4.png)
![Monitoring](https://i.imgur.com/8SZxGp5.png)
![Scaling](https://i.imgur.com/9SZxGp6.png)

## Overview

## ✅ Deliverable

A fully deployed and optimized application with:

- Working production deployment
- Proper monitoring and analytics
- Configured backup systems
- Security measures in place
- Performance optimizations
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
12-second-deployment/
  README.md
  final/         # Your completed solution goes here
  deployment/    # Deployment configuration
    frontend/
      netlify.toml
      _redirects
      monitoring/
        analytics.js
        error-tracking.js
    backend/
      pythonanywhere/
        wsgi.py
        requirements.txt
        monitoring/
          logging.py
          metrics.py
  docs/          # Deployment documentation
    monitoring.md
    analytics.md
    backup.md
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
