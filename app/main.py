from fastapi import FastAPI, APIRouter
from app.models.client.views import router as routes_client
from app.models.room.views import router as room_views
from app.models.staff.views import router as staff_views
from app.models.group_request.views import router as group_request_views
from app.models.room_occupancy.views import router as room_occupancy_views
from app.models.booking.views import router as booking_views
from app.models.client.repositpries import ClientRepositories
from app.models.room.repositpries import RoomRepositories
from app.models.group_request.repositpries import Group_requestRepositories
from app.models.room_occupancy.repositpries import Room_occupancyRepositories
from app.models.booking.repositpries import BookingRepositories
from app.models.staff.repositpries import StaffRepositories

# Инициализируем репозитории

from app.pages.router import router as router_pages

app = FastAPI()
app.include_router(routes_client)
app.include_router(room_views)
app.include_router(staff_views)
app.include_router(router_pages)
app.include_router(group_request_views)
app.include_router(room_occupancy_views)
app.include_router(booking_views)

router = APIRouter()

@router.get("/count/all")
async def count_all():
    # Собираем количество записей для всех репозиториев
    room_occupancy_count = await Room_occupancyRepositories.count()
    room_count = await RoomRepositories.count()
    group_request_count = await Group_requestRepositories.count()
    client_count = await ClientRepositories.count()
    booking_count = await BookingRepositories.count()
    staff_count = await StaffRepositories.count()  # добавлено, потому что не было описано в схемах

    # Возвращаем данные
    return {
        "room_occupancy": room_occupancy_count,
        "room": room_count,
        "group_request": group_request_count,
        "client": client_count,
        "booking": booking_count
    }
