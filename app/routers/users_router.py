from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.services.services_for_models.user import UserServices

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def registration_users(
    session: AsyncSession = Depends(get_session),
    service: UserServices = Depends(UserServices),
):
    return await service.get_user(session)
