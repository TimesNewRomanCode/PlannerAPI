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


    async def newsletter_true_for_user(
        self,
        session: AsyncSession,
        chat_id: int,
    ):
        chat_id = str(chat_id)
        user = await user_repository.get_by_chat_id(session, chat_id)
        if user:
            user.is_newsletter = True
            await session.commit()
        else:
            print("Такого пользователя нет")

        return user


    async def newsletter_false_for_user(
        self,
        session: AsyncSession,
        chat_id: int,
    ):
        chat_id = str(chat_id)
        user = await user_repository.get_by_chat_id(session, chat_id)
        if user:
            user.is_newsletter = False
            await session.commit()
        else:
            print("Такого пользователя нет")

        return user
