from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.enums import TicketStatus, TicketPriority
from app.database import base
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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

    assigned_user_id= Column(Integer, ForeignKey("users.id"), nullable=True)
    assigned_user=relationship("User", back_populates="tickets")


class User(base):
    __tablename__= "users"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)
    email= Column(String, unique=True)
    tickets = relationship("Ticket", back_populates="assigned_user")

#"ForeignKey defines the relationship in the database by linking one table to another and enforcing referential integrity. relationship defines the relationship in SQLAlchemy's ORM, allowing us to access related Python objects such as user.tickets or ticket.assigned_user without writing explicit join queries."