
# Notes / Todo REST API (Django)

A backend REST API built using **Django** and **Django REST Framework** that allows authenticated users to manage their personal notes or todo items.  
This project demonstrates clean backend architecture, secure API design, and professional development practices.


## Project Overview

This application provides a set of secure REST APIs that enable users to:

*   Create notes or todo items
*   View their own notes
*   Update existing notes
*   Delete notes
*   Access data securely using token‑based authentication

The project is designed as a **backend service** that can later be integrated with a web or mobile frontend.


## Key Features

*   User‑specific notes (each user sees only their own data)
*   Token‑based authentication
*   Full CRUD functionality (Create, Read, Update, Delete)
*   RESTful API design
*   Django Admin Panel for internal data management
*   Automated API tests
*   Clean and scalable project structure


##  Tech Stack

*   **Python 3**
*   **Django**
*   **Django REST Framework**
*   **SQLite** (development database)
*   **Token Authentication**
*   **Postman** (for API testing)


## Project Structure

    todo_api/
    │
    ├── todo_api/              # Project configuration
    │
    ├── notes/                 # Notes application
    │   ├── models.py          # Database models
    │   ├── serializers.py     # API serializers
    │   ├── views.py           # API views
    │   ├── urls.py            # API routes
    │   ├── tests.py           # Automated tests
    │
    ├── manage.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore


## Setup Instructions

Follow the steps below to run the project locally.


### 1 Clone the Repository

    git clone <repository-url>
    cd todo_api


### 2️ Create and Activate Virtual Environment

    python -m venv venv

**Activate virtual environment**

**macOS / Linux**

    source venv/bin/activate

**Windows**

    venv\Scripts\activate


### 3 Install Dependencies

    pip install -r requirements.txt


### 4 Run Database Migrations

    python manage.py makemigrations
    python manage.py migrate


### 5 Create Superuser (Admin Account)

    python manage.py createsuperuser

This user will be used for:

*   Admin panel access
*   Token generation


### 6 Start the Development Server

    python manage.py runserver 8001

Server will run at:

    http://127.0.0.1:8001/


##  Authentication

The API uses **token‑based authentication**.

### Generate Token for a User

    python manage.py shell

<!---->

    from django.contrib.auth.models import User
    from rest_framework.authtoken.models import Token

    user = User.objects.get(username="your_username")
    token, _ = Token.objects.get_or_create(user=user)
    print(token.key)



### Using Token in API Requests

Add the following header in Postman or any API client:

    Authorization: Token <your_token_here>



## API Endpoints

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| GET    | `/api/notes/`      | Retrieve all user notes |
| POST   | `/api/notes/`      | Create a new note       |
| PUT    | `/api/notes/{id}/` | Update an existing note |
| DELETE | `/api/notes/{id}/` | Delete a note           |



## Testing the APIs

### Manual Testing

*   APIs are tested using **Postman**
*   Supports GET, POST, PUT, and DELETE requests
*   Token authentication is required for all endpoints

### Automated Testing

Automated API tests are included.

    python manage.py test

Tests cover:

*   Authentication
*   CRUD operations
*   Unauthorized access handling



##  Admin Panel

Django Admin Panel is available at:

    http://127.0.0.1:8001/admin/

The admin panel is used to:

*   Manage users
*   View and manage notes
*   Verify API‑created data












