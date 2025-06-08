# Prok Professional Networking

## 📚 Table of Contents

- [What You’ll Build](#-what-youll-build)
- [What You Will Do?](#-what-you-will-do)
- [Learning Outcomes](#-learning-outcomes)
- [Folder Structure](#-folder-structure)
- [Tech Stack](#-tech-stack)
- [How to Run the App](#-how-to-run-the-app)
- [Daily Task Breakdown](#-daily-task-breakdown)
- [Checkpoints & Milestones](#-checkpoints--milestones)
- [Preview Screens](#-preview-screens)
- [Extra Learning Resources](#-extra-learning-resources)

![App Screenshot](https://placehold.co/800x400?text=Prok+Professional+Networking+App+Screenshot)

---

## 🎯 What You’ll Build

A real-world, full-stack professional networking platform inspired by LinkedIn! You’ll create user authentication, profiles, posts, connections, messaging, job boards, and more—step by step, just like a real developer.

---

## 📋 What You Will Do?

| Module              | Description                                                               | Screenshots                                                                                                                           | Guide                                      |
| ------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Login & Signup UI   | Build the Login & Signup UI with React and Tailwind CSS.                  | <img src="01-login-signup-ui/Login.png" alt="Login" width="400"/> <img src="01-login-signup-ui/Signup.png" alt="Signup" width="400"/> | [README](01-login-signup-ui/README.md)     |
| Setup Auth          | Implement backend authentication: registration and login with Flask.      | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](02-setup-auth/README.md)          |
| Profile Page        | Create and edit user profile pages with real-world fields and validation. | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](03-profile-page/README.md)        |
| User Profile Page   | Build a detailed user profile page with editable sections.                | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](04-user-profile-page/README.md)   |
| Create a Post       | Implement the UI and logic for users to create new posts.                 | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](05-create-a-post/README.md)       |
| Posts               | Build post creation and feed components, connect to backend API.          | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](06-posts/README.md)               |
| Feed                | Display a user's feed with posts and updates, using React and Flask.      | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](07-feed/README.md)                |
| Feed with Posts     | Enhance the feed with richer post content and user interactions.          | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](08-feed-with-posts/README.md)     |
| Connection Requests | Add screens for sending, accepting, and managing connection requests.     | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](09-connection-requests/README.md) |
| Connections         | Manage user connections: send, accept, decline, and view connections.     | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](10-connections/README.md)         |
| Messaging           | Real-time or async user messaging with chat UI and backend integration.   | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](11-messaging/README.md)           |
| Messaging Screen    | Build a dedicated messaging screen for conversations.                     | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](12-messaging-screen/README.md)    |
| Job Board           | List jobs, allow users to apply, and manage job applications.             | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](13-job-board/README.md)           |
| Jobs                | Implement job listing and application management features.                | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](14-jobs/README.md)                |
| Responsive UI       | Make the app responsive for all devices and screen sizes.                 | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](15-responsive-ui/README.md)       |
| Styling             | Enhance the app's visual design and user experience with modern styling.  | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](16-styling/README.md)             |
| Deployment          | Deploy the full-stack app to a production environment.                    | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](17-deployment/README.md)          |
| Deployment View     | Create a deployment status or success screen.                             | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](18-deployment-view/README.md)     |
| Advanced Features   | Add advanced features, optimizations, or integrations to the application. | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](19-advanced/README.md)            |
| Resume Builder      | Build a resume builder tool for users to create and download resumes.     | <img src="https://placehold.co/800x400?text=No+Image" alt="No Image" width="400"/>                                                    | [README](20-resume-builder/README.md)      |

---

## 🧠 Learning Outcomes

- Build a modern web app with React (frontend) and Flask (backend)
- Implement authentication, user profiles, posts, connections, and messaging
- Connect frontend and backend using REST APIs
- Practice real-world project structure and teamwork
- Deploy a full-stack app to production

---

## 📁 Folder Structure

```
Prok-Professional-Networking/
├── app/
│   ├── backend/         # Flask backend
│   └── frontend/        # React frontend
├── 01-login-signup-ui/  # Daily/Module folders (see below)
├── ...
├── README.md            # This guide
```

---

## 🛠 Tech Stack

- **Frontend:** React, Tailwind CSS
- **Backend:** Flask (Python)
- **Database:** (You choose: SQLite, PostgreSQL, etc.)
- **Other:** REST API, JWT Auth, WebSockets (for messaging)

---

## 🪜 How to Run the App

1. **Clone the Repo**
   ```bash
   git clone https://github.com/your-username/prok-professional-networking.git
   cd Prok-Professional-Networking
   ```
2. **Install Frontend Dependencies**
   ```bash
   cd app/frontend
   npm install
   ```
3. **Install Backend Dependencies**
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```
4. **Start the Backend**
   ```bash
   flask run
   ```
5. **Start the Frontend**
   ```bash
   cd ../frontend
   npm start
   ```
6. **Open in Browser**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:5000](http://localhost:5000)

💡 **Pro Tip:** If you get stuck, check each module’s README for focused help!

---

## 🔨 Daily Task Breakdown

Below are suggested ways to tackle the project, whether you’re working solo or as a team. Each day/module focuses on a real-world screen or feature, not just frontend/backend code.

### 👤 1-Member Team (Solo Path)

| Day | Module/Screen       | What You’ll Build/Do                                                                          |
| --- | ------------------- | --------------------------------------------------------------------------------------------- |
| 1   | Login & Signup UI   | Design and implement login/signup screens with form validation and user feedback.             |
| 2   | Setup Auth          | Build backend registration/login endpoints and connect UI to backend for real authentication. |
| 3   | Profile Page        | Create user profile view/edit screens, including form validation and profile picture upload.  |
| 4   | User Profile Page   | Build a detailed user profile page with editable sections.                                    |
| 5   | Create a Post       | Implement the UI and logic for users to create new posts.                                     |
| 6   | Posts               | Display posts in a feed, enable interactions (like, comment, etc.).                           |
| 7   | Feed                | Build the main feed screen, fetching and displaying posts from all users.                     |
| 8   | Feed with Posts     | Enhance the feed with richer post content and user interactions.                              |
| 9   | Connection Requests | Add screens for sending, accepting, and managing connection requests.                         |
| 10  | Connections         | Manage user connections: view, remove, and interact with connections.                         |
| 11  | Messaging           | Create chat/messaging screens and enable real-time or async messaging.                        |
| 12  | Messaging Screen    | Build a dedicated messaging screen for conversations.                                         |
| 13  | Job Board           | List jobs, allow users to apply, and manage job applications.                                 |
| 14  | Jobs                | Implement job listing and application management features.                                    |
| 15  | Responsive UI       | Make the app responsive for all devices and screen sizes.                                     |
| 16  | Styling             | Polish the UI, add modern styling, and improve accessibility.                                 |
| 17  | Deployment          | Deploy the app, set up environment variables, and test in production.                         |
| 18  | Deployment View     | Create a deployment status or success screen.                                                 |
| 19  | Advanced Features   | Add bonus features (e.g., notifications, analytics, search, etc.).                            |
| 20  | Resume Builder      | Build a resume builder tool for users to create and download resumes.                         |

### 👥 2-Member Team (Pair Path)

| Day | Member 1 (Screen/Module)  | Member 2 (Screen/Module) |
| --- | ------------------------- | ------------------------ |
| 1   | Login Screen              | Signup Screen            |
| 2   | Auth API (register/login) | Connect UI to Auth API   |
| 3   | Profile View              | Profile Edit             |
| 4   | User Profile Page         | Create a Post            |
| 5   | Posts                     | Feed                     |
| 6   | Feed with Posts           | Connection Requests      |
| 7   | Connections               | Messaging                |
| 8   | Messaging Screen          | Job Board                |
| 9   | Jobs                      | Responsive UI            |
| 10  | Styling                   | Deployment               |
| 11  | Deployment View           | Advanced Features        |
| 12  | Resume Builder            | (shared tasks)           |

### 👨‍👩‍👧 3-Member Team (Trio Path)

| Day | Member 1 (Screen/Module)  | Member 2 (Screen/Module) | Member 3 (Screen/Module) |
| --- | ------------------------- | ------------------------ | ------------------------ |
| 1   | Login Screen              | Signup Screen            | Welcome/Landing Screen   |
| 2   | Auth API (register/login) | Connect UI to Auth API   | Error/Feedback Screens   |
| 3   | Profile View              | Profile Edit             | Profile Picture/Settings |
| 4   | User Profile Page         | Create a Post            | Feed                     |
| 5   | Posts                     | Feed with Posts          | Connection Requests      |
| 6   | Connections               | Messaging                | Messaging Screen         |
| 7   | Job Board                 | Jobs                     | Responsive UI            |
| 8   | Styling                   | Deployment               | Deployment View          |
| 9   | Advanced Features         | Resume Builder           | (shared tasks)           |

> 💡 **Tip:** For teams, communicate daily and merge your work often. Each member should own a screen or feature, not just a layer (frontend/backend), for a real-world experience.

---

## ✅ Checkpoints & Milestones

- [ ] User can register and log in
- [ ] User can edit their profile
- [ ] Users can create and view posts
- [ ] Users can connect with others
- [ ] Real-time messaging works
- [ ] Job board is functional
- [ ] App is deployed and live!

Celebrate each milestone—you’re building a real app!

---

## 📸 Preview Screens

> Add your own screenshots or GIFs as you build! Here are some ideas:

- Login & Signup UI
- User Profile Page
- Feed with Posts
- Connections & Messaging
- Job Board

---

## 📚 Extra Learning Resources

- [React Docs](https://react.dev/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/)
- [Python Official Docs](https://docs.python.org/3/)

---

> 💡 **Keep going! Every step you take is real-world developer practice.**
