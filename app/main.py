from unittest import skip

from fastapi import FastAPI, HTTPException
from app.database import engine, base, get_db
from app.models import Ticket, User
from app.enums import TicketStatus, TicketPriority

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.schemas import TicketCreate, TicketResponse, TicketUpdate, UserCreate, UserResponse

base.metadata.create_all(bind=engine)


app=FastAPI()

tickets=[]

@app.get("/")
def home():
    return {"message":"Welcome to the Ticket Management System!"}

@app.get("/tickets",response_model=list[TicketResponse])
def get_tickets(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    tickets = db.query(Ticket).offset(skip).limit(limit).all()
    return tickets

@app.get("/tickets/search", response_model=list[TicketResponse])
def search_tickets(title:str, db:Session=Depends(get_db)):
    tickets=db.query(Ticket).filter(Ticket.title.ilike(f"%{title}%")).all()
    return tickets

@app.get("/tickets/unassigned")
def get_unassigned_tickets(db:Session=Depends(get_db)):
    tickets=db.query(Ticket).filter(Ticket.assigned_user_id.is_(None)).all()
    return tickets

@app.get("/tickets/status/{status}")
def get_tickets_by_status(status:TicketStatus, db:Session=Depends(get_db)):
    tickets=db.query(Ticket).filter(Ticket.status==status).all()
    return tickets


@app.get("/tickets/{ticket_id}",response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticketnot found")
    return ticket


@app.post("/tickets")
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(title=ticket.title, description=ticket.description, status=ticket.status, assigned_user_id=ticket.assigned_user_id, priority=ticket.priority)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, updated_ticket: TicketUpdate, db:Session= Depends(get_db)):
    ticket=db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket.title=updated_ticket.title
    ticket.description=updated_ticket.description

    db.commit()
    db.refresh(ticket)

    return ticket

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id:int, db: Session=Depends(get_db)):
    ticket=db.query(Ticket).filter(Ticket.id==ticket_id).first()

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted successfully"}



@app.post("/users")
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
#"Exception catches every possible error, including programming mistakes. It's better to catch IntegrityError because we know we're specifically handling a database constraint violation."
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already exists")

    return new_user
    

@app.get("/users")
def get_users(db: Session=Depends(get_db)):
    users=db.query(User).all()
    return users

@app.get("/users/{user_id}",response_model=UserResponse)
def get_user(user_id:int, db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/{user_id}/tickets",response_model=list[TicketResponse])
def get_user_tickets(user_id:int, db:Session=Depends(get_db)):
    #tickets=db.query(Ticket).filter(Ticket.assigned_user_id==user_id).all()
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.tickets

@app.put("/tickets/{ticket_id}/assign/{user_id}")
def assign_ticket(ticket_id:int, user_id:int, db:Session=Depends(get_db)):
    ticket=db.query(Ticket).filter(Ticket.id==ticket_id).first()
    user=db.query(User).filter(User.id==user_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    ticket.assigned_user_id=user_id
    db.commit()
    db.refresh(ticket)
    return ticket

