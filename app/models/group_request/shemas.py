from pydantic import BaseModel
from datetime import date

class SNewGroupRequests(BaseModel):
    client_id: int
    request_data: date
    number_of_people: int
    request_status: str
    
