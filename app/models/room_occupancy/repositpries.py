from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.room_occupancy.models import Room_occupancy
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class Room_occupancyRepositories(BaseRepositories):
    model = Room_occupancy