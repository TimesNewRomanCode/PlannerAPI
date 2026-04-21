from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.schemas.schedule import ScheduleAlien, ScheduleMe, ScheduleGroup
from app.services.schedule.get_schedule import ScheduleService
from app.services.services_for_models.groups import GroupService

router = APIRouter(prefix="/schedule", tags=["schedule"])

@router.post("/groups")
async def get_groups_for_schedule(
    data: ScheduleGroup,
    session: AsyncSession = Depends(get_session),
    service: GroupService = Depends(GroupService),
):
    return await service.get_groups_array_by_user_sid(session, data.user_sid)

@router.post("/me_schedule")
async def schedule_get_by_sid_and_date(
        data: ScheduleMe,
        session: AsyncSession = Depends(get_session),
        service: ScheduleService = Depends(ScheduleService),
):
    return await service.get_photo_by_user_sid_and_date(session, data.user_sid, data.date)

@router.post("/alien_schedule")
async def schedule_get_by_group_sid_and_date(
        data: ScheduleAlien,
        session: AsyncSession = Depends(get_session),
        service: ScheduleService = Depends(ScheduleService),
):
    return await service.get_photo_by_group_sid_and_date(session, data.group_sid, data.date)