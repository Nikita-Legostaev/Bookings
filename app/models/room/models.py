from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Room(Base):
    __tablename__='room'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    root_type: Mapped[str]
    status: Mapped[str]
    price_for_night: Mapped[int]