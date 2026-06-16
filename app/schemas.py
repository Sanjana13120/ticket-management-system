from pydantic import BaseModel
from app.enums import TicketStatus, TicketPriority

#TicketCreate(BaseModel) is a Pydantic schema used for request validation and data transfer between client and API.
class TicketCreate(BaseModel):
    title: str
    description: str
    status: TicketStatus = TicketStatus.OPEN
    priority: TicketPriority = TicketPriority.MEDIUM

class TicketUpdate(BaseModel):
    title: str
    description: str