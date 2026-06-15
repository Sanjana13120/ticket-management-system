from fastapi import FastAPI
from app.database import engine, base, get_db
from app.models import Ticket

from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas import TicketCreate, TicketUpdate

base.metadata.create_all(bind=engine)


app=FastAPI()

tickets=[]

@app.get("/")
def home():
    return {"message":"Welcome to the Ticket Management System!"}

@app.get("/tickets")
# def get_tickets():
#     return tickets
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        return {"error": "Ticket not found"}
    return ticket


@app.post("/tickets")

# def create_ticket(title: str):
#     ticket = {"id" : len(tickets)+1, "title": title}
#     tickets.append(ticket)
#     return tickets
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(title=ticket.title, description=ticket.description)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, updated_ticket: TicketUpdate, db:Session= Depends(get_db)):
    ticket=db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        return {"error": "Ticket not found"}
    
    ticket.title=updated_ticket.title
    ticket.description=updated_ticket.description

    db.commit()
    db.refresh(ticket)

    return ticket

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id:int, db: Session=Depends(get_db)):
    ticket=db.query(Ticket).filter(Ticket.id==ticket_id).first()

    if ticket is None:
        return {"error": "Ticket not found"}
    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted successfully"}
    