from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.enums import TicketStatus, TicketPriority
from app.database import base
from datetime import datetime

#Ticket(Base) is a SQLAlchemy model used to map Python classes to database tables. It defines the structure of the "tickets" table in the database, with columns for id, title, description, and status. Each instance of the Ticket class represents a row in the "tickets" table, allowing for easy interaction with the database using SQLAlchemy's ORM capabilities.
class Ticket(base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status= Column(Enum(TicketStatus),default=TicketStatus.OPEN)  
    priority= Column(Enum(TicketPriority),default=TicketPriority.MEDIUM)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
