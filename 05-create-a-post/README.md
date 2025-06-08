# Day 4: Create a Post

## 🎯 Goal

Build the **Create a Post** module for the Prok Professional Networking app. This module guides you through designing and implementing a user-friendly post creation form, validating input, and connecting the frontend to the backend API for saving posts.

## 📚 Learning Outcomes

- Design and implement a post creation form (text, image, etc.) using React and Tailwind CSS.
- Validate user input and provide clear, user-friendly error messages.
- Integrate the form with the backend API to save posts.
- Display loading indicators, success, and error feedback to the user.
- Practice real-world form handling, API integration, and UX best practices.

## 📸 Preview

<!-- Add a screenshot of the post creation form here when available -->

## 🛠️ Tasks

1. **Setup the Project**

   - Clone the repository and navigate to the `05-create-a-post` folder.
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

   - Build a user-friendly post creation form using React and Tailwind CSS.
   - Include fields for post content (text) and optional image upload.
   - Add clear labels, placeholders, and helpful validation messages.
   - Use React state to manage form data and feedback.
   - Show loading indicators while submitting, and reset the form on success.

3. **Form Validation**

   - Ensure required fields (e.g., post text) are filled.
   - Validate input length and file types (if supporting images).
   - Display user-friendly error messages for invalid input.

4. **Backend Integration**

   - Use fetch/axios to send post data to the backend API.
   - Handle API responses and errors gracefully.
   - Show success messages on successful post creation and error states if submission fails.

5. **(Optional) Enhance User Experience**

   - Add image preview before upload.
   - Support drag-and-drop for images.
   - Allow users to tag others or add hashtags.
   - Provide real-time feedback (e.g., character count, image size warning).

6. **Testing**
   - Test the form with different input scenarios (empty, invalid, large files, etc.).
   - Ensure the UI updates correctly based on API responses.

## 💡 Why It Matters

Posting is a core feature of any social or professional network. This module gives you hands-on experience with forms, validation, and API integration—skills you’ll use in almost every real-world web project.

## 🚀 Pro Tips

- Use React state and controlled components for form management.
- Keep your UI responsive and accessible.
- Review backend API docs to ensure your request format matches expectations.
- Use try/catch for error handling in async functions.
- Modularize your code for easier maintenance and testing.

## ✅ Deliverable

A working post creation form that connects to the backend, validates input, and provides clear feedback to the user. Push your solution to the `/final` folder when done.

---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x and pip

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd 05-create-a-post
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
   - Open your browser and go to `http://localhost:3000/create-post` to access the post creation form.
   - Backend API runs on `http://localhost:5000` by default.

---

## 🗂️ Folder Structure

```
05-create-a-post/
  README.md
  final/         # Your completed solution goes here
  starter/       # Starter code and assets
  backend/       # Flask backend code
    app.py
    requirements.txt
    models/
      post.py
  frontend/      # React frontend code
    package.json
    src/
      index.jsx
```

---

## 📝 Document Your Bonus Improvement

Describe your bonus improvement here. For example:

> **Bonus Improvement:** Added image preview and drag-and-drop support for post images, making the post creation process more interactive and user-friendly.

---

If you have any questions or need help, feel free to open an issue or reach out to the instructor.

---
