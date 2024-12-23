from pydantic import BaseModel
from datetime import date

class SNewBooking(BaseModel):
    client_id: int
    room_id: int
    check_in_date: date
    check_out_date: date
    booking_status: str
