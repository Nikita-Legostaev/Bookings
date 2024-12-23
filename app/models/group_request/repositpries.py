from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.group_request.models import Group_request
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class Group_requestRepositories(BaseRepositories):
    model = Group_request