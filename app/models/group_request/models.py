from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Group_request(Base):
    __tablename__='group_request'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    request_data: Mapped[Date] = mapped_column(type_=Date)
    number_of_people: Mapped[int]
    request_status: Mapped[str]
    