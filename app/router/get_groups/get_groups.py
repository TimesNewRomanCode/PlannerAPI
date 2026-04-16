from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.schemas.group import GroupGet
from app.services.services_for_models.groups import GroupService

router = APIRouter(prefix="/get_groups", tags=["get_groups"])

@router.post("/")
async def registration(
    data: GroupGet,
    session: AsyncSession = Depends(get_session),
    service: GroupService = Depends(GroupService),
):
    print(data)
    await service.update_groups(session, data.AddressName, data.GroupsList)
    return {"status": "ok"}