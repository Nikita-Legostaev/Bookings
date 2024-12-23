from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.client.views import get_all_client
from app.models.room.views import get_all_rooms
from app.models.staff.views import get_all_staff
from app.models.booking.views import get_all_booking
from app.models.group_request.views import get_all_groupRequests
from app.models.room_occupancy.views import get_all_room_occupancy
from app.models.client.repositpries import ClientRepositories
from app.models.room.repositpries import RoomRepositories
from app.models.group_request.repositpries import Group_requestRepositories
from app.models.room_occupancy.repositpries import Room_occupancyRepositories
from app.models.booking.repositpries import BookingRepositories
from app.models.staff.repositpries import StaffRepositories



router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/client')
async def get_client_html(request: Request, client=Depends(get_all_client)):
    return templates.TemplateResponse(name='client.html', context={'request': request, 'client': client})

@router.get('/rooms')
async def get_rooms_html(request: Request, rooms=Depends(get_all_rooms)):
    return templates.TemplateResponse(name='rooms.html', context={'request': request, 'rooms': rooms})

@router.get('/staff')
async def get_staff_html(request: Request, staff=Depends(get_all_staff)):
    return templates.TemplateResponse(name='staff.html', context={'request': request, 'staff': staff})

@router.get('/booking')
async def get_booking_html(request: Request, booking=Depends(get_all_booking)):
    return templates.TemplateResponse(name='booking.html', context={'request': request, 'booking': booking})

@router.get('/group_request')
async def get_group_request_html(request: Request, group_requests=Depends(get_all_groupRequests)):
    return templates.TemplateResponse(name='group_request.html', context={'request': request, 'group_requests': group_requests})

@router.get('/room_occupancy')
async def get_room_occupancy_html(request: Request, room_occupancy=Depends(get_all_room_occupancy)):
    return templates.TemplateResponse(name='room_occupancy.html', context={'request': request, 'room_occupancy': room_occupancy})


from app.models.client.repositpries import ClientRepositories
from app.models.room.repositpries import RoomRepositories
from app.models.group_request.repositpries import Group_requestRepositories
from app.models.room_occupancy.repositpries import Room_occupancyRepositories
from app.models.booking.repositpries import BookingRepositories
from app.models.staff.repositpries import StaffRepositories

@router.get('/count')
async def get_counts_html(
    request: Request,
    room_occupancy_count=Depends(Room_occupancyRepositories.count),  # Подсчет производителей
    room_count=Depends(RoomRepositories.count),        # Подсчет категорий
    group_request_count=Depends(Group_requestRepositories.count),             # Подсчет продуктов
    client_count=Depends(ClientRepositories.count), # Подсчет характеристик продуктов
    booking_count=Depends(BookingRepositories.count),           # Подсчет поставок
    staff_count=Depends(StaffRepositories.count) 
                       
                       
):
    # Подготовка данных для диаграммы
    counts_data = {
        'Room Occupancy': room_occupancy_count,
        'Rooms': room_count,
        'Group Requests': group_request_count,
        'Clients': client_count,
        'Bookings': booking_count,
        'Staff': staff_count
    }

    return templates.TemplateResponse(
        'counts.html', 
        context={'request': request, 'counts_data': counts_data}
    )