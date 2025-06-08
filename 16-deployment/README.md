# Day 9: Deployment

## 🎯 Goal

Build the **Deployment** module of the Prok Professional Networking app. This module covers deploying both frontend and backend to a production environment.

## 📚 Learning Outcomes

- Understand the core concepts of deploying web applications.
- Learn how to prepare React and Flask apps for production.
- Implement deployment scripts and environment configuration.
- Learn best practices for security, scalability, and maintainability.

## 📸 Preview

![Preview](./starter/preview.png)

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `day9-deployment` folder.
   - Ensure all dependencies are installed for both frontend and backend.

2. **Prepare for Deployment**

   - Build the React frontend for production:
     ```bash
     cd frontend
     npm run build
     ```
   - Set up environment variables for both frontend and backend.
   - Update Flask backend configuration for production (e.g., disable debug mode).

3. **Deployment Implementation**

   - Choose a deployment platform (e.g., Heroku, Vercel, AWS, DigitalOcean).
   - Deploy the backend (Flask) to your chosen platform.
   - Deploy the frontend (React) to your chosen platform or serve it via Flask.
   - Configure domain, SSL, and environment variables as needed.

4. **Testing**
   - Test the deployed application end-to-end.
   - Ensure all features work as expected in production.
   - Monitor logs and fix any deployment issues.

## 🧪 Bonus Challenge

- Add an extra improvement, such as:
  - Automated deployment with GitHub Actions or similar CI/CD tools.
  - Custom domain and SSL setup.
  - Performance monitoring and error tracking.
- Document your improvement in your own words at the end of this README.

## ✅ Deliverable

A deployed, production-ready Prok Professional Networking module, with links and documentation, pushed to GitHub in the `/final` folder.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip
- Accounts on deployment platforms (e.g., Heroku, Vercel, AWS)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd day9-deployment
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
3. **Build and Deploy**
   - Build frontend:
     ```bash
     cd frontend
     npm run build
     ```
   - Deploy backend and frontend as per your chosen platform's instructions.

---

## 🗂️ Folder Structure

```
day9-deployment/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Set up automated deployment to Heroku using GitHub Actions. This ensures every push to main triggers a new deployment automatically.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
