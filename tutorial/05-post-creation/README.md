# Day 5: Post Creation UI

## 🎯 Goal

Build Post Creation UI (frontend) and implement the necessary backend logic for storing posts.

## 📚 Learning Outcomes

- Create post creation interface.
- Implement rich text editing.
- Handle media uploads.
- Create post storage system.
- Implement post validation.
- Design user-friendly post creation flow.

## 🚀 Getting Started

Ensure your Day 4 Profile Backend is complete and working. You should understand rich text editing and media handling. The backend and frontend should be set up and running.

## 🛠️ Tasks

1.  **Create and Switch to a New Branch**

    > **IMPORTANT:** Always create a new branch for each distinct piece of work.

    ```bash
    # First, ensure you are on your 'master' branch and it's up-to-date
    git checkout master
    git pull origin master  # Get any potential updates from your own fork's master

    # Now, create and switch to a new branch for this day's assignment/feature
    git checkout -b day-5-post-creation
    ```

    > **What's happening?** You're creating an independent line of development for this day's tasks.

2.  **Set Up Development Environment**

    - **Backend Virtual Environment (if not already active):**
      ```bash
      cd backend
      source venv/bin/activate  # On Windows use: venv\Scripts\activate
      ```
    - **Install Additional Dependencies:**
      ```bash
      pip install Flask Flask-SQLAlchemy Flask-Migrate Pillow python-magic
      ```
    - **Frontend (already set up from previous days):**
      - Ensure your frontend directory has all Node.js dependencies installed via:
        ```bash
        npm install
        ```

3.  **Frontend Implementation**

    - **Create Post Creation Form:**
      - Design a form for post content, including sections for text, media, and a preview.
      - Implement a rich text editor for the main post body to allow formatted input.
      - Add functionality for media uploads (images/videos).
      - Create a post preview component to show how the post will look before submission.
      - Implement client-side form validation for post content and media, along with loading states during submission.

4.  **Backend Implementation**

    - **Create Post Model and Endpoints:**
      - Define a `Post` database model with fields such as `id`, `user_id` (foreign key to the User model), `content`, `media_url` (nullable), `created_at`, etc.
      - Implement the `POST /api/posts` endpoint for handling post creation requests.
      - Set up the necessary logic for media storage and validation on the server side.
      - Add post metadata and consider initial indexing for future search functionality.

5.  **Media Handling**

    - **Implement Image and Video Upload:**
      - Set up file upload handling on the backend for both images and videos.
      - Validate uploaded file types and sizes to ensure they meet requirements.
      - Process and securely store media files on the server (e.g., in a dedicated uploads folder).
      - Generate accessible media URLs that the frontend can use to display the uploaded content.

6.  **Run the Application**

    ```bash
    # Start the backend server (in one terminal)
    cd backend
    flask run

    # Start the frontend development server (in another terminal)
    cd frontend
    npm run dev
    ```

    The application will be available at:

    - Frontend: `http://localhost:3000/create-post`
    - Backend API: `http://localhost:5000`

7.  **Testing**

    - Test post creation with text-only content.
    - Test post creation with both text and image media.
    - Test post creation with both text and video media.
    - Test media uploads for various image and video formats/sizes.
    - Test form validation and ensure appropriate error handling is displayed.
    - Test loading states and user feedback during post submission.

## 🔄 Git Workflow

1.  **Develop and Save Progress**

    ```bash
    git add .
    git commit -m "Day 5: Implement post creation UI and backend logic"
    ```

2.  **Push Your Changes to Your Fork**

    ```bash
    git push -u origin day-5-post-creation
    ```

3.  **Merge After Completion**

    ```bash
    git checkout master
    git pull origin master
    git merge day-5-post-creation
    git push origin master
    ```

## 📸 Preview

<img src="post-creation.png" alt="Post Creation UI" width="120"/>

![Create Post Desktop View](create-post-desk.png)
![Create Post Mobile View](create-post-mobile.png)

## ✅ Deliverable

A fully functional post creation system with:

- Rich text editing.
- Media upload and preview.
- Proper validation and error handling.
- Clean, documented code.
- All tests passing.
