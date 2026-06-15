from sqlalchemy import Column, Integer, String
from app.database import base

#Ticket(Base) is a SQLAlchemy model used to map Python classes to database tables. It defines the structure of the "tickets" table in the database, with columns for id, title, description, and status. Each instance of the Ticket class represents a row in the "tickets" table, allowing for easy interaction with the database using SQLAlchemy's ORM capabilities.
class Ticket(base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status= Column(String, default="open")
