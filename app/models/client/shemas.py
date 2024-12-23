from pydantic import BaseModel
from datetime import date

class SNewClient(BaseModel):
    full_name: str
    contact: str
    passport_number: str
    registry_date: date
