from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Booking(Base):
    __tablename__='booking'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    check_in_date: Mapped[Date] = mapped_column(type_=Date)
    check_out_date: Mapped[Date] = mapped_column(type_=Date)
    booking_status: Mapped[str]