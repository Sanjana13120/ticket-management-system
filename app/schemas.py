from datetime import datetime

from pydantic import BaseModel, ConfigDict
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

class UserResponse(BaseModel):
    id: int
    name:str
    email:str
#"This input is a SQLAlchemy object. Read its attributes (user.id, user.name, etc.) instead of expecting a dictionary."
    model_config= ConfigDict(from_attributes=True)

class TicketResponse(BaseModel):
    id: int
    title: str
    description:str
    status: TicketStatus
    priority: TicketPriority
    assigned_user_id: int | None
    created_at: datetime
    updated_at: datetime

    model_config=ConfigDict(from_attributes=True)