# ✅ Task Manager API (Django REST Framework)

A simple Django REST API to manage tasks securely using JWT authentication. Built using function-based views (`@api_view`) to keep it beginner-friendly.

---

## 🔧 Setup Instructions

### 1. Clone the Repository
Clone this project to your local machine using Git.

### 2. Create a Virtual Environment
Use `venv` or `virtualenv` to isolate your environment.

### 3. Install Requirements
Install dependencies using `pip install -r requirements.txt`.

### 4. Run Migrations
Apply migrations using `python manage.py migrate`.

### 5. Create Superuser (Optional)
Create an admin account to access the Django admin panel.

### 6. Start Development Server
Run the server locally with `python manage.py runserver`.

---

## 📦 API Endpoints

| Method | Endpoint               | Description              | Auth Required |
|--------|------------------------|--------------------------|----------------|
| POST   | `/api/register/`       | Register a new user      | ❌             |
| POST   | `/api/token/`          | Obtain JWT token         | ❌             |
| POST   | `/api/token/refresh/`  | Refresh JWT token        | ❌             |
| GET    | `/api/tasks/`          | List user's tasks        | ✅             |
| POST   | `/api/tasks/`          | Create a new task        | ✅             |
| GET    | `/api/tasks/<id>/`     | Retrieve specific task   | ✅             |
| PUT    | `/api/tasks/<id>/`     | Update specific task     | ✅             |
| DELETE | `/api/tasks/<id>/`     | Delete specific task     | ✅             |

---

## 🧱 Models Structure & Details

### User Model

- Utilizes Django’s built-in `User` model.
- Fields: `username`, `password`, `email` (optional).
- Handles authentication using JWT (`djangorestframework-simplejwt`).

### Task Model

- `user`: ForeignKey to the authenticated user who owns the task.
- `title`: Short title or summary of the task.
- `description`: Optional detailed description of the task.
- `completed`: Boolean indicating whether the task is finished.
- `created_at`: Timestamp automatically added when the task is created.

Each task is user-specific and isolated by authentication. Only logged-in users can view, create, update, or delete their own tasks.

---

## 📁 Project Structure Overview

- `taskmanager/`: Project-level settings and routing.
- `tasks/`: App containing models, serializers, views, and task-specific routing.
- `requirements.txt`: Dependencies list.
- `README.md`: Project instructions and structure (this file).

---

## ✅ Features

- User Registration & JWT Authentication
- CRUD operations on personal tasks
- Clean, simple, and secure REST API
- Built using Django REST Framework with function-based views
