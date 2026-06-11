from fastapi import FastAPI

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