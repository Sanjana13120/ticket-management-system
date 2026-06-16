#Enums restrict a field to a predefined set of values. In this case, the TicketStatus enum defines three possible statuses for a ticket: OPEN, IN_PROGRESS, and CLOSED. By using an enum, we can ensure that the status of a ticket can only be one of these predefined values, which helps maintain data integrity and consistency in the application.
from enum import Enum

class TicketStatus(Enum):
    OPEN ="OPEN"
    IN_PROGRESS="IN_PROGRESS"
    CLOSED="CLOSED"

class TicketPriority(Enum):
    LOW="LOW"
    MEDIUM="MEDIUM"
    HIGH="HIGH"