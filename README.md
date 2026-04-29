
# Notes / Todo REST API (Django + JWT)

This project is a backend REST API built using **Django** and **Django REST Framework**.  
It allows authenticated users to securely create, view, update, and delete their personal notes or todo items.

The application uses **JWT (JSON Web Token) authentication** and follows standard backend development and Git workflow practices.

---

##  Project Overview

The Notes / Todo API provides secure REST endpoints for managing user-specific notes.  
Each user can access only their own data through authenticated API requests.

The project is designed as a backend service that can later be integrated with a web or mobile frontend.

---

## Features

- JWT-based authentication (Access & Refresh tokens)
- User-specific notes (data isolation)
- Full CRUD operations (Create, Read, Update, Delete)
- Secure REST APIs
- Django Admin Panel support
- Automated API tests
- Clean and scalable project structure

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (development database)
- Postman (API testing)

---

##  Project Structure

```

todo\_api/
│
├── todo\_api/              # Project settings
│
├── notes/                 # Notes application
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

````

---

##  Setup Instructions

### 1️ Clone the Repository

```bash
git clone <repository-url>
cd todo_api
````

***

### 2️ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Activate the virtual environment**

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```



### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```



### 4️ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

***

### 5 Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```



### 6️ Run Development Server

   bash
python manage.py runserver 8001


Application will be available at:

    http://127.0.0.1:8001/

***

##  Authentication (JWT)

This project uses **JWT authentication** via `djangorestframework-simplejwt`.



### Obtain Access & Refresh Token (Login)

**POST**

    /api/token/

**Request Body**

```json
{
  "username": "<your_username>",
  "password": "<your_password>"
}
```

**Response**

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```



### 🔓 Access Secured APIs

Include the **access token** in request headers:

    Authorization: Bearer <access_token>



### 🔄 Refresh Access Token

**POST**

    /api/token/refresh/

**Request Body**
   json
{
  "refresh": "<refresh_token>"
}


***

## API Endpoints

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| GET    | `/api/notes/`         | Retrieve user notes  |
| POST   | `/api/notes/`         | Create a new note    |
| PUT    | `/api/notes/{id}/`    | Update a note        |
| DELETE | `/api/notes/{id}/`    | Delete a note        |
| POST   | `/api/token/`         | JWT login            |
| POST   | `/api/token/refresh/` | Refresh access token |

***

## Testing

Automated tests are included for API validation.

bash
python manage.py test


Tests cover:

*   Authentication
*   CRUD operations
*   Unauthorized access handling



##  Admin Panel

Django Admin Panel is available at:

    http://127.0.0.1:8001/admin/

The admin panel allows:

*   User management
*   Note management
*   Data verification


