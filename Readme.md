# Ticket Management System

Backend ticket management system built using FastAPI, PostgreSQL and SQLAlchemy.

## Features
- Create Ticket
- Get all Ticket
- Get Ticket by ID
- Update Ticket
- Delete Ticket

## Tech Stack
- Python
- FastAPI
- Git
- PostgreSQL
- SQLAlchemy
- Pydantic 
- Uvicorn

## API Endpoints
# Create Ticket

POST /tickets

# Get All Tickets

GET /tickets

# Get Ticket By ID

GET /tickets/{id}

# Update Ticket

PUT /tickets/{id}

# Delete Ticket

DELETE /tickets/{id}


## Run

pip install -r requirements.txt
uvicorn app.main:app --reload

## Swagger Documentation

Open: http://127.0.0.1:8000/docs