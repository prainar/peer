# Day 9: Feed Interactions

## 🎯 Goal

Enhance the Feed with Basic Interactions (e.g., liking/commenting placeholders) and ensure responsiveness.

## 📚 Learning Outcomes

- Implement post interaction features
- Create real-time updates
- Design interaction animations
- Handle user feedback
- Implement interaction states
- Create engaging user experience

## 🚀 Getting Started

Ensure your Day 8 Basic Feed is complete and tested. You should understand WebSocket basics and React animations. The backend and frontend should be set up and running.

## 🛠️ Tasks

### Create and Switch to a New Branch

> **IMPORTANT:** Always create a new branch for each distinct piece of work.

```bash
# First, ensure you are on your 'main' branch and it's up-to-date
git checkout main
git pull origin main  # Get any potential updates from your own fork's main

# Now, create and switch to a new branch for this day's assignment/feature
git checkout -b day-9-feed-interactions
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
pip install Flask Flask-SQLAlchemy Flask-Migrate flask-socketio
```

#### Frontend (already set up from previous days):

Ensure your frontend directory has all Node.js dependencies installed via `npm install`.

### Interaction Features

#### Implement Like, Comment, and Share

- Add like button and counter to each post
- Implement comment section with live updates
- Add share and bookmark options
- Implement reaction system and interaction counters

### Real-time Updates

#### Set Up WebSocket and Live Interactions

- Set up WebSocket connection using flask-socketio
- Implement real-time likes and live comment updates
- Create notification system for new interactions
- Handle connection states and fallback mechanisms

### User Experience

#### Enhance Interactions and Feedback

- Add interaction animations and feedback states
- Implement loading indicators and error handling
- Create success messages and undo actions

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

- Frontend: http://localhost:3000/feed
- Backend API: http://localhost:5000

### Testing

- Test all interaction features (like, comment, share, bookmark)
- Test real-time updates and notifications
- Test error handling and loading states
- Test animations and responsiveness

## 🔄 Git Workflow

### Develop and Save Your Progress

```bash
git add .
git commit -m "Day 9: Implement feed interactions and real-time updates"
```

### Push Your Changes to Your Fork

```bash
git push -u origin day-9-feed-interactions
```

### Merge After Completion

```bash
git checkout main
git pull origin main
git merge day-9-feed-interactions
git push origin main
```

## 📸 Preview

<img src="feed-interactions.png" alt="Feed Interactions UI" width="120"/>

## ✅ Deliverable

A fully interactive feed system with:

- Real-time updates for likes and comments
- Engaging user experience and feedback
- Proper error handling and loading states
- Clean, documented code
- All tests passing

## 🗂️ Folder Structure

```
09-feed-interactions/
  README.md
  final/         # Your completed solution goes here
  backend/       # Flask backend code
    app.py
    requirements.txt
    routes/
      interactions.py
    services/
      websocket.py
      interaction_service.py
    utils/
      realtime.py
  frontend/      # React frontend code
    package.json
    src/
      components/
        Interactions/
          LikeButton.jsx
          CommentSection.jsx
          ShareButton.jsx
          ReactionPicker.jsx
      hooks/
        useInteractions.js
        useWebSocket.js
      services/
        interactions.js
```

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.
