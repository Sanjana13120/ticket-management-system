from pydantic import BaseModel

#TicketCreate(BaseModel) is a Pydantic schema used for request validation and data transfer between client and API.
class TicketCreate(BaseModel):
    title: str
    description: str

class TicketUpdate(BaseModel):
    title: str
    description: str