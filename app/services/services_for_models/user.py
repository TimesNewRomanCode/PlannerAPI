import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import user_repository
from app.schemas.user import UserCreate

class UserServices:
    async def register_user(
        self, session: AsyncSession, group_sid: uuid, username: str
    ):
        user = await user_repository.create(
            session,
            obj_in=UserCreate(
                sid=uuid.uuid4(),
                username=username,
                is_active=True,
                group_sid=group_sid
            ),
        )
        return user.sid

    async def get_user(self, session: AsyncSession):
        user = await user_repository.get_all(session)
        return user
