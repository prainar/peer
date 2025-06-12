# Day 14: Messaging Backend

## 🎯 Goal

Integrate Messaging Backend Logic (Flask) to send and receive messages.

## 📚 Learning Outcomes

- Implement WebSocket server
- Create message handling system
- Design message storage
- Implement real-time updates
- Create message delivery system
- Handle message persistence

## 🚀 Getting Started

Ensure your Day 13 Messaging UI is complete and tested. You should understand WebSocket and database design. The backend and frontend should be set up and running.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-14-messaging-backend
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
pip install Flask-SocketIO python-socketio SQLAlchemy
```

#### Frontend (already set up from previous days):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Backend Implementation

#### Set Up WebSocket Server

- Configure WebSocket server
- Create message endpoints
- Implement message storage
- Add message validation
- Create message delivery system
- Implement message history

### Real-time Features

#### Implement WebSocket Events

- Set up WebSocket event handlers
- Create typing indicator system
- Add read receipt functionality
- Implement online status tracking
- Create message status system
- Add notification service

### Data Management

#### Design Message System

- Create message schema
- Implement message queries
- Set up message indexing
- Add message search functionality
- Implement message deletion
- Create message archiving system

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

- Frontend: http://localhost:3000/messages
- Backend API: http://localhost:5000

### Testing

- Test WebSocket connections
- Test message delivery system
- Test real-time features
- Test message storage
- Test error handling
- Test system performance

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 14: Implement messaging backend with WebSocket support"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-14-messaging-backend
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-14-messaging-backend
git push origin main
```

## 📸 Preview

![WebSocket Architecture](https://i.imgur.com/4TZxGp1.png)
![Message Queue](https://i.imgur.com/5TZxGp2.png)
![Database Schema](https://i.imgur.com/6TZxGp3.png)

## Overview

## ✅ Deliverable

A robust messaging backend system with:

- Working WebSocket server
- Complete message handling
- Real-time features
- Data persistence
- Error handling
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
14-messaging-backend/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      message.py
      conversation.py
    routes/
      messages.py
    services/
      websocket.py
      message_service.py
    utils/
      validation.py
  frontend/      # React frontend code
    package.json
    src/
      services/
        messages.js
        websocket.js
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
