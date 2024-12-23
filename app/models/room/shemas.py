from pydantic import BaseModel, ConfigDict

class SNewRooms(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    root_type: str
    status: str
    price_for_night: int