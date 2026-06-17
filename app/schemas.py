from pydantic import BaseModel
from app.enums import TicketStatus, TicketPriority

#TicketCreate(BaseModel) is a Pydantic schema used for request validation and data transfer between client and API.
class TicketCreate(BaseModel):
    title: str
    description: str
    status: TicketStatus = TicketStatus.OPEN
    priority: TicketPriority = TicketPriority.MEDIUM
    assigned_user_id: int | None = None  # Optional field for assigned user ID

class TicketUpdate(BaseModel):
    title: str
    description: str


class UserCreate(BaseModel):
    name: str
    email: str