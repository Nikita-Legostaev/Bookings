from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Client(Base):
    __tablename__='client'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str]
    contact: Mapped[str]
    passport_number: Mapped[str]
    registry_date: Mapped[Date] = mapped_column(type_=Date)
    