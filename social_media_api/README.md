# Social Media API

**Social Media API** is a Django REST Framework application that provides a backend for a social media platform. It supports user registration, authentication, user following, posts, likes, notifications, and an aggregated feed. This API is designed for deployment in production and is currently hosted on . https://alx-social-media-api.onrender.com


---

## Features

* **User Authentication**: Register, login, and view profiles.
* **Following System**: Users can follow and unfollow others.
* **Posts**: Users can create and view posts.
* **Feed**: Aggregated feed of posts from followed users.
* **Likes**: Users can like or unlike posts.
* **Notifications**: Receive notifications for new followers, likes, and comments.

---

## Technologies

* Python 3.12
* Django 6.x
* Django REST Framework
* PostgreSQL (hosted on Render)
* Gunicorn (WSGI server for production)
* Render (hosting)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Mistire/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
```

### Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # Linux / macOS
env\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file or set environment variables in your deployment environment with:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.onrender.com
DATABASE_URL=postgres://user:password@hostname:port/dbname
```

---

## Database

The project uses PostgreSQL. To configure locally:

1. Install PostgreSQL and create a database.
2. Set the `DATABASE_URL` environment variable, e.g.:

```env
DATABASE_URL=postgres://username:password@localhost:5432/social_media_db
```

3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## API Endpoints

### Accounts

* `POST /api/accounts/register/` — Register a new user
* `POST /api/accounts/login/` — Login and receive token
* `GET /api/accounts/profile/` — View current user profile
* `POST /api/accounts/follow/<int:user_id>/` — Follow a user
* `POST /api/accounts/unfollow/<int:user_id>/` — Unfollow a user

### Posts

* `GET /api/posts/feed/` — View feed of followed users’ posts
* `POST /api/posts/<int:pk>/like/` — Like a post
* `POST /api/posts/<int:pk>/unlike/` — Unlike a post

### Notifications

* `GET /api/notifications/` — Retrieve notifications for the current user

All endpoints require authentication via token, except registration and login.

---

## Deployment

This project is deployed on [Render](https://render.com).

### Build & Start Commands

* **Build Command:**

```bash
pip install -r requirements.txt
```

* **Start Command:**

```bash
gunicorn social_media_api.wsgi
```

Set the root directory in Render to:

```
Alx_DjangoLearnLab/social_media_api
```

---

## Testing

Use Postman, curl, or any API client to test endpoints. Example:

```bash
curl -X POST https://your-render-url/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username":"user1", "password":"password123"}'
```

---