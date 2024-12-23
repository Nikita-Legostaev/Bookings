from pydantic import BaseModel
from datetime import date

class SNewRoomOccupancy(BaseModel):
    staff_id: int
    room_id: int
    start_date: date
    end_date: date
    
