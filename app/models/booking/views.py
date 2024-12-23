from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.booking.repositpries import BookingRepositories
from app.models.booking.shemas import SNewBooking


router = APIRouter(
    prefix="/booking",
    tags=["booking"],
)


@router.get("/all")
async def get_all_booking(offset: int = 0, limit: int = 10):
    all_booking = await BookingRepositories.get_all()
    return all_booking[offset:limit]

@router.post("/add_booking")
async def add_booking(
    SNewBooking: SNewBooking,
):
    added_booking = await BookingRepositories.add(
        client_id=SNewBooking.client_id,
        room_id=SNewBooking.room_id,
        check_in_date=SNewBooking.check_in_date,
        check_out_date=SNewBooking.check_out_date,
        booking_status=SNewBooking.booking_status,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{booking_id}")
async def remove_booking(
    booking_id: int,
):
    booking = await BookingRepositories.find_one_or_none(id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Не найдена")
    await BookingRepositories.delete(id=booking_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{booking_id}")
async def update_booking(
    booking_id: int,
    SNewBooking: SNewBooking,  
    ):
    booking = await BookingRepositories.find_by_id(id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Не найден")
    await BookingRepositories.update(id=booking_id, **SNewBooking.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/count")
async def count_stock():
    count = await BookingRepositories.count()
    return {"count": count}
