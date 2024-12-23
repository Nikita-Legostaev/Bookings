from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.group_request.repositpries import Group_requestRepositories
from app.models.group_request.shemas import SNewGroupRequests


router = APIRouter(
    prefix="/groupRequests",
    tags=["groupRequests"],
)


@router.get("/all")
async def get_all_groupRequests(offset: int = 0, limit: int = 10):
    all_groupRequests = await Group_requestRepositories.get_all()
    return all_groupRequests[offset:limit]

@router.post("/add_groupRequests")
async def add_groupRequests(
    SNewGroupRequests: SNewGroupRequests,
):
    added_groupRequests = await Group_requestRepositories.add(
        client_id=SNewGroupRequests.client_id,
        request_data=SNewGroupRequests.request_data,
        number_of_people=SNewGroupRequests.number_of_people,
        request_status=SNewGroupRequests.request_status,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{groupRequests_id}")
async def remove_groupRequests(
    groupRequests_id: int,
):
    groupRequests = await Group_requestRepositories.find_one_or_none(id=groupRequests_id)
    if not groupRequests:
        raise HTTPException(status_code=404, detail="Не найдена")
    await Group_requestRepositories.delete(id=groupRequests_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{groupRequests_id}")
async def update_groupRequests(
    groupRequests_id: int,
    SNewGroupRequests: SNewGroupRequests,  
    ):
    groupRequests = await Group_requestRepositories.find_by_id(id=groupRequests_id)
    if not groupRequests:
        raise HTTPException(status_code=404, detail="Не найден")
    await Group_requestRepositories.update(id=groupRequests_id, **SNewGroupRequests.model_dump())
    return {"detail": "Успешно изменёно"}


@router.get("/count")
async def count_stock():
    count = await Group_requestRepositories.count()
    return {"count": count}