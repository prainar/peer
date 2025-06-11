# Day 1: Project Setup

## 🎯 Goal

Set up the development environment and create the initial project structure for a professional networking application.

## 📚 Learning Outcomes

- Set up development environment
- Initialize project structure
- Configure basic dependencies
- Create initial documentation
- Understand project architecture
- Set up version control

## 🚀 Getting Started

## 🛠️ Tasks

1. **Project Setup**

**Create and Switch to a New Branch**

> **IMPORTANT:** Never work directly on the main branch! Always create a new branch for each assignment or distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for your assignment/feature
# Choose a descriptive name, e.g., 'assignment-1-login-form' or 'feature-user-profile'
git checkout -b your-assignment-branch-name
```

> **What's happening?** You're creating an independent line of development. The main branch in your fork should ideally remain a clean copy of the original template. Your new branch is where you'll make all your assignment-specific changes.

2.**Set Up Development Environment**

```bash
# Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Create project directories
mkdir -p frontend backend
cd frontend

# Initialize React project with Vite
npm create vite@latest . -- --template react-ts

# Set up backend structure
cd ../backend
mkdir -p app tests
touch requirements.txt
```

3.**Install Dependencies**

```bash
# Install frontend dependencies
cd frontend (one Terminal)
npm install

# Install backend dependencies
cd ../backend (Another Terminal)
pip install -r requirements.txt
```

4.**Frontend Implementation**

**Login Page/Component:**
_ **Inputs:** Fields for `username`, (or `email`) and `password`.
_ **Action:** A "Login" button to submit credentials.
_ **Navigation:** A link to redirect users to the "Signup" page.
_ **Validation:** Basic client-side validation to ensure required fields are not empty.

- **Signup Page/Component:**
  _ **Inputs:** Fields for `username`, `email`, `password`, and `confirm_password`.
  _ **Action:** A "Signup" button to register a new user.
  _ **Navigation:** A link to redirect users to the "Login" page.
  _ **Validation:**
  _ Required field checks for all inputs.
  _ Password length validation (minimum 8 characters). \* Confirmation that `password` and `confirm_password` fields match.

  5.**Run the Application**

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

  6.**Testing**

  - Test form validation
  - Test responsive design

### Git Workflow

1.**Develop and Save Your Progress**

As you code and complete parts of your assignment, regularly save your progress to Git:

```bash
# Check the status of your changes (see what files you've modified)
git status

# Add changes to the staging area
# Use 'git add .' to add all changes in the current directory
# Or 'git add path/to/file.js' to add specific files
git add .

# Commit your changes with a descriptive message
# Make your messages clear and concise!
git commit -m "Assignment X: Brief description of changes"
```

- `git status`: Shows which files you've modified, added, or deleted
- `git add .`: Moves your modified or new files into the staging area (a waiting room for your changes)
- `git commit -m "Your message"`: Takes a snapshot of the changes in your staging area and saves them permanently in your branch's history

  2.**Push Your Changes to Your Fork**

Once you're ready to save your work online or submit your assignment:

```bash
# Push your branch to YOUR remote fork
# The first time you push a new branch, use '-u' to link your local branch
# to its remote counterpart. For subsequent pushes, 'git push' is often enough
git push -u origin your-assignment-branch-name
```

> **Note:** This uploads your local branch to your origin (your personal fork)

3.**Merge After Assignment Completion**

After your assignment is complete and submitted:

```bash
git checkout main           # Switch to your local main
git pull origin main        # Ensure your local main is up-to-date with your remote main
git merge assignment-1-feature # Merge the feature branch into your main
git push origin main        # Push the updated main to your fork online
```

```

## 📸 Preview

<img src="login-signup.png" alt="Login Signup UI" width="120"/>

## ✅ Deliverable

A working project setup with login/signup UI, properly version controlled with Git.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
```
