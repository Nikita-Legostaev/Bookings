from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Staff(Base):
    __tablename__='staff'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str]
    position: Mapped[str]
    contact: Mapped[str]
    work_schedule: Mapped[str]