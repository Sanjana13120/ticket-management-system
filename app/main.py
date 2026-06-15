from fastapi import FastAPI
from app.database import engine, base
from app.models import Ticket

base.metadata.create_all(bind=engine)


app=FastAPI()

tickets=[]

@app.get("/")
def home():
    return {"message":"Welcome to the Ticket Management System!"}

@app.get("/tickets")
def get_tickets():
    return tickets

@app.post("/tickets")
def create_ticket(title: str):
    ticket = {"id" : len(tickets)+1, "title": title}
    tickets.append(ticket)
    return tickets
