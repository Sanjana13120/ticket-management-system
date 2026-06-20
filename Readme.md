# Ticket Management System API

A RESTful Ticket Management System built with FastAPI, SQLAlchemy, and PostgreSQL. This project provides APIs for managing users and support tickets, including ticket assignment, status filtering, search functionality, and pagination.

## Features

### User Management

* Create User
* Get User Details
* Get User's Tickets

### Ticket Management

* Create Ticket
* Get All Tickets
* Get Ticket By ID
* Update Ticket
* Delete Ticket

### Additional Features

* Assign Ticket to User
* Filter Tickets by Status
* Get Unassigned Tickets
* Search Tickets by Title
* Pagination Support

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy ORM
* PostgreSQL
* Pydantic
* Uvicorn

## Project Structure

```text
ticket-management-system/
│
├── app/
│   ├── models/
│   ├── schemas/
│   ├── enums/
│   ├── database/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Sanjana13120/ticket-management-system
cd ticket-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

Update your database connection settings in your configuration file.

Example PostgreSQL URL:

```text
postgresql://username:password@localhost:5432/ticketdb
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```
## API Documentation

Swagger UI provides interactive API testing.

![Swagger UI](screenshots/swagger-ui.png)

## API Endpoints

### User APIs

| Method | Endpoint            | Description      |
| ------ | ------------------- | ---------------- |
| POST   | /users              | Create User      |
| GET    | /users/{id}         | Get User         |
| GET    | /users/{id}/tickets | Get User Tickets |

### Ticket APIs

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | /tickets      | Create Ticket    |
| GET    | /tickets      | Get All Tickets  |
| GET    | /tickets/{id} | Get Ticket By ID |
| PUT    | /tickets/{id} | Update Ticket    |
| DELETE | /tickets/{id} | Delete Ticket    |

### Additional APIs

| Method | Endpoint                       | Description            |
| ------ | ------------------------------ | ---------------------- |
| PUT    | /tickets/{id}/assign/{user_id} | Assign Ticket          |
| GET    | /tickets/status/{status}       | Filter By Status       |
| GET    | /tickets/unassigned            | Get Unassigned Tickets |
| GET    | /tickets/search                | Search By Title        |
| GET    | /tickets?skip=0&limit=10       | Pagination             |

## Concepts Demonstrated

* FastAPI Routing
* SQLAlchemy ORM
* PostgreSQL Integration
* Pydantic Validation
* Response Models
* Database Relationships
* Query Parameters
* Pagination
* Search Functionality
* Dependency Injection
* Exception Handling

## Future Improvements

* JWT Authentication
* Role-Based Access Control
* Alembic Migrations
* Docker Support
* Unit Testing
* Deployment

## Author

Developed as a backend learning project using FastAPI, SQLAlchemy, and PostgreSQL.
