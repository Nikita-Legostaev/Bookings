from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.staff.repositpries import StaffRepositories
from app.models.staff.shemas import SNewStaff


router = APIRouter(
    prefix="/staff",
    tags=["staff"],
)


@router.get("/all")
async def get_all_staff(offset: int = 0, limit: int = 10):
    all_staff = await StaffRepositories.get_all()
    return all_staff[offset:limit]

@router.post("/add_staff")
async def add_staff(
    SNewStaff: SNewStaff,
):
    added_staff = await StaffRepositories.add(
        full_name=SNewStaff.full_name,
        position=SNewStaff.position,
        contact=SNewStaff.contact,
        work_schedule=SNewStaff.work_schedule,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{staff_id}")
async def remove_staff(
    staff_id: int,
):
    staff = await StaffRepositories.find_one_or_none(id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Не найдена")
    await StaffRepositories.delete(id=staff_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{staff_id}")
async def update_staff(
    staff_id: int,
    SNewStaff: SNewStaff,  
    ):
    staff = await StaffRepositories.find_by_id(id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Не найден")
    await StaffRepositories.update(id=staff_id, **SNewStaff.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/count")
async def count_stock():
    count = await StaffRepositories.count()
    return {"count": count}
