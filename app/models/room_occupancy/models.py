from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Room_occupancy(Base):
    __tablename__='room_occupancy'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    staff_id: Mapped[int] = mapped_column(ForeignKey('staff.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    start_date: Mapped[Date] = mapped_column(type_=Date)
    end_date: Mapped[Date] = mapped_column(type_=Date)