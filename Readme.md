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
Create Ticket     - POST/tickets
Get All Tickets   - GET/tickets
Get Ticket by ID  - GET/tickets/{ID} 
Update Ticket     - PUT/ticket/{ID}
Delete Ticket     - DELETE/tickets/{ID}

## Run

pip install -r requirements.txt
uvicorn app.main:app --reload

## Swagger Documentation

Open: http://127.0.0.1:8000/docs