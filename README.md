# FastAPI CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI and SQLAlchemy, complete with JWT authentication. It supports PostgreSQL or MySQL databases for storing users and tasks data.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Authentication](#authentication)
- [License](#license)

## Features

- CRUD operations for Users and Tasks
- User Authentication with JWT
- Protected API endpoints

## Requirements

- Python 3.7+
- PostgreSQL or MySQL
- [Pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-crud-app.git
   cd fastapi-crud-app
   ```

2. **Create Virtual Environment (Windows):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Database Configuration

Open `app/database.py` and update the `SQLALCHEMY_DATABASE_URL` with your PostgreSQL or MySQL credentials:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

### JWT Secret Key

Open `app/auth.py` and replace the `SECRET_KEY` with a secure, random key:

```python
SECRET_KEY = "your-new-secret-key"
```

## Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

## Endpoints Overview

- **Create User**: `POST /users/`
- **Fetch User**: `GET /users/{user_id}`
- **Create Task**: `POST /tasks/`
- **List Tasks**: `GET /tasks/`
- **JWT Token**: `POST /token`

## Authentication

### Obtain a JWT Token

Send a `POST` request to `/token` with form data including:

- `username` (email)
- `password`

### Access Protected Endpoints

Include the JWT token in the Authorization header:

```bash
curl -X GET http://127.0.0.1:8000/tasks/ -H "Authorization: Bearer <your_token>"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.