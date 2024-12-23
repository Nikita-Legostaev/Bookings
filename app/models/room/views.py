from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.room.repositpries import RoomRepositories
from app.models.room.shemas import SNewRooms



router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
)


@router.get("/all")
async def get_all_rooms(offset: int = 0, limit: int = 10):
    all_rooms = await RoomRepositories.get_all()
    return all_rooms[offset:limit]

@router.post("/add_rooms")
async def add_rooms(
    SNewRooms: SNewRooms,
):
    added_rooms = await RoomRepositories.add(
        root_type=SNewRooms.root_type,
        status=SNewRooms.status,
        price_for_night=SNewRooms.price_for_night,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{rooms_id}")
async def remove_rooms(
    rooms_id: int,
):
    rooms = await RoomRepositories.find_one_or_none(id=rooms_id)
    if not rooms:
        raise HTTPException(status_code=404, detail="Не найдена")
    await RoomRepositories.delete(id=rooms_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{rooms_id}")
async def update_rooms(
    rooms_id: int,
    SNewRooms: SNewRooms,  
    ):
    rooms = await RoomRepositories.find_by_id(id=rooms_id)
    if not rooms:
        raise HTTPException(status_code=404, detail="Не найден")
    await RoomRepositories.update(id=rooms_id, **SNewRooms.model_dump())
    return {"detail": "Успешно изменёно"}


@router.get("/count")
async def count_stock():
    count = await RoomRepositories.count()
    return {"count": count}