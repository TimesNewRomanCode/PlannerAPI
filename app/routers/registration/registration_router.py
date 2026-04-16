from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.schemas.address import AddressRegistration
from app.schemas.group import GroupRegistration
from app.schemas.user import UserRegistration
from app.services.services_for_models.address import AddressServices
from app.services.services_for_models.college import CollegeServices
from app.services.services_for_models.groups import GroupService
from app.services.services_for_models.user import UserServices

router = APIRouter(prefix="/registration", tags=["registration"])

@router.get("/colleges")
async def registration_get_colleges(
    session: AsyncSession = Depends(get_session),
    service: CollegeServices = Depends(CollegeServices),
):
    return await service.get_colleges_by_registration(session)

@router.post("/address")
async def registration_get_address(
    data: AddressRegistration,
    session: AsyncSession = Depends(get_session),
    service: AddressServices = Depends(AddressServices),
):
    return await service.get_addresses_array_by_college_sid(session, data.college_sid)

@router.post("/groups")
async def registration_get_groups(
    data: GroupRegistration,
    session: AsyncSession = Depends(get_session),
    service: GroupService = Depends(GroupService),
):
    return await service.get_groups_array_by_address_sid(session, data.address_sid)

@router.post("/register")
async def registration_users(
    data: UserRegistration,
    session: AsyncSession = Depends(get_session),
    service: UserServices = Depends(UserServices),
):
    return await service.register_user(session,data.group_sid, data.username)





