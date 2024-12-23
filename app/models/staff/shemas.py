from pydantic import BaseModel

class SNewStaff(BaseModel):
    full_name: str
    position: str
    contact: str
    work_schedule: str