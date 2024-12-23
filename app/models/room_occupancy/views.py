from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.room_occupancy.repositpries import Room_occupancyRepositories
from app.models.room_occupancy.shemas import SNewRoomOccupancy



router = APIRouter(
    prefix="/room_occupancy",
    tags=["room_occupancy"],
)


@router.get("/all")
async def get_all_room_occupancy(offset: int = 0, limit: int = 10):
    all_room_occupancy = await Room_occupancyRepositories.get_all()
    return all_room_occupancy[offset:limit]

@router.post("/add_room_occupancy")
async def add_room_occupancy(
    SNewRoomOccupancy: SNewRoomOccupancy,
):
    added_room_occupancy = await Room_occupancyRepositories.add(
        staff_id=SNewRoomOccupancy.staff_id,
        room_id=SNewRoomOccupancy.room_id,
        start_date=SNewRoomOccupancy.start_date,
        end_date=SNewRoomOccupancy.end_date,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{room_occupancy_id}")
async def remove_room_occupancy(
    room_occupancy_id: int,
):
    room_occupancy = await Room_occupancyRepositories.find_one_or_none(id=room_occupancy_id)
    if not room_occupancy:
        raise HTTPException(status_code=404, detail="Не найдена")
    await Room_occupancyRepositories.delete(id=room_occupancy_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{room_occupancy_id}")
async def update_room_occupancy(
    room_occupancy_id: int,
    SNewRoomOccupancy: SNewRoomOccupancy,  
    ):
    room_occupancy = await Room_occupancyRepositories.find_by_id(id=room_occupancy_id)
    if not room_occupancy:
        raise HTTPException(status_code=404, detail="Не найден")
    await Room_occupancyRepositories.update(id=room_occupancy_id, **SNewRoomOccupancy.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/count")
async def count_stock():
    count = await Room_occupancyRepositories.count()
    return {"count": count}
